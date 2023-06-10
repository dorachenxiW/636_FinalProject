from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import re
from datetime import datetime
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

dbconn = None
connection = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/admin")
def admin():
    return render_template("adminbase.html")

@app.route("/listmembers")
def listmembers():
    connection = getCursor()
    sql = """SELECT members.FirstName, members.LastName, members.MemberID, teams.TeamName, members.City, members.Birthdate
          FROM members
          INNER JOIN teams
          ON members.TeamID = teams.TeamID;"""
    connection.execute(sql)
    memberList = connection.fetchall()
    #print(memberList)
    return render_template("memberlist.html", memberlist = memberList)    

@app.route("/listmembers/athlete/detail", methods=['GET', 'POST'])
def athlete_detail():
    memberid = request.form.get('id')
    connection = getCursor()
    sql="""SELECT members.FirstName, members.LastName, members.MemberID, events.EventName, event_stage.StageDate, event_stage.StageName, 
           event_stage.Location, event_stage.Qualifying, event_stage_results.Position, event_stage_results.PointsScored
           FROM events JOIN event_stage on events.EventID=event_stage.EventID 
           JOIN event_stage_results on event_stage.StageID=event_stage_results.StageID
           JOIN members on event_stage_results.MemberID=members.MemberID WHERE members.MemberID=%s;"""
    connection.execute(sql, (memberid,))
    Details = connection.fetchall()
    sql_name="SELECT FirstName, LastName FROM members WHERE MemberID=%s;"
    connection.execute(sql_name, (memberid,))
    Names=connection.fetchone()
    if len(Details) == 0:
        return render_template ("athlete_nocurrentinfo.html", memberid=memberid, names=Names)
    else:
        return render_template("athlete.html", details=Details)

@app.route("/listevents")
def listevents():
    connection = getCursor()
    connection.execute("SELECT * FROM events;")
    eventList = connection.fetchall()
    return render_template("eventlist.html", eventlist = eventList)

@app.route("/admin/search")
def search():
    return render_template("search.html")

@app.route("/admin/search/result_member", methods=["POST"])
def searchresult_member():
    searchterm = request.form.get('membersearch')
    #sprint(searchterm)
    likesearchterm = f'%{searchterm}%'
    connection = getCursor()
    connection.execute("SELECT members.FirstName, members.LastName, members.MemberID, teams.TeamName, members.City, members.Birthdate\
          FROM members INNER JOIN teams ON members.TeamID = teams.TeamID WHERE members.FirstName LIKE %s;", (likesearchterm,))
    memberList = connection.fetchall()
    #print(memberList)
    return render_template("search.html", memberlist = memberList) 

@app.route("/admin/search/result_event", methods=["POST"])
def searchresult_event():
    searchterm = request.form.get('eventsearch')
    #print(searchterm)
    likesearchterm = f'%{searchterm}%'
    connection = getCursor()
    connection.execute("SELECT * FROM events WHERE EventName LIKE %s;", (likesearchterm,))
    eventList = connection.fetchall()
    return render_template("search.html", eventlist=eventList) 

@app.route("/admin/addeditmember")
def addeditmember():
    connection = getCursor()
    sql1 = "SELECT * FROM members;"
    connection.execute(sql1)
    memberList = connection.fetchall()
    sql2="SELECT * FROM teams;"
    connection.execute(sql2)
    teamList=connection.fetchall()
    return render_template("addeditmember.html", memberlist=memberList, teamlist=teamList)

@app.route("/admin/member/add", methods=["POST"])
def addmembers():
    #memberid=request.form.get('MemberID')
    teamid=request.form.get('TeamID')
    firstname=request.form.get('FirstName')
    lastname=request.form.get('LastName')
    city=request.form.get('City')
    birthdate=request.form.get('Birthdate')

    connection = getCursor()
    connection.execute("INSERT INTO members (TeamID, FirstName, LastName, City, Birthdate) VALUES (%s, %s, %s, %s, %s);", (teamid, firstname, lastname, city, birthdate, ))
    
    return redirect ("/admin/addeditmember")

@app.route("/admin/member/edit/<memberid>")
def editmember(memberid):
    #print(memberid)
    connection=getCursor()
    sql1 = "SELECT * FROM members WHERE memberid=%s;"
    connection.execute(sql1, (memberid,))
    memberEditing=connection.fetchone()
    sql2="SELECT * FROM teams;"
    connection.execute(sql2)
    teamList=connection.fetchall()
    return render_template ("editmember.html", memberediting=memberEditing, teamlist=teamList)

@app.route("/admin/updatemember",  methods=["POST"])
def updatemember():
    memberid=request.form.get('MemberID')
    teamid=request.form.get('TeamID')
    firstname=request.form.get('FirstName')
    lastname=request.form.get('LastName')
    city=request.form.get('City')
    birthdate=request.form.get('Birthdate')

    connection = getCursor()
    connection.execute("UPDATE members SET TeamID=%s, FirstName=%s, LastName=%s, City=%s, Birthdate=%s WHERE MemberID=%s;", (teamid, firstname, lastname, city, birthdate, memberid,))

    return redirect ("/admin/addeditmember")

@app.route("/admin/addeventsandstages")
def addeventsandstages():
    connection = getCursor()
    sql1 = "SELECT * FROM events;"
    connection.execute(sql1)
    eventList = connection.fetchall()
    sql2="SELECT * FROM teams;"
    connection.execute(sql2)
    teamList=connection.fetchall()
    return render_template("addevents.html", eventlist=eventList, teamlist=teamList)

@app.route("/admin/event/add", methods=["POST"])
def addevent():
    eventname=request.form.get('EventName')
    sport=request.form.get('Sport')
    nzteamid=request.form.get('NZTeam')
    connection=getCursor()
    connection.execute("INSERT INTO events (EventName, Sport, NZTeam) VALUES (%s, %s, %s);", (eventname, sport, nzteamid,))

    return redirect ("/admin/addeventsandstages")

@app.route("/admin/eventstage/add/<eventid>")
def currentstages(eventid):
    connection=getCursor()
    sql = "SELECT * FROM events INNER JOIN event_stage on event_stage.EventID=events.EventID WHERE events.EventID=%s;"
    connection.execute(sql, (eventid,))
    stageList=connection.fetchall()
    sql_eventname="SELECT EventName FROM events WHERE EventID=%s;"
    connection.execute(sql_eventname, (eventid,))
    EventName=connection.fetchone()
    if len(stageList) == 0:
        return render_template ("addeventstage_nocurrentstage.html", eventname=EventName, eventid=eventid)
    else:
        return render_template ("addeventstage.html", stagelist=stageList)

@app.route("/admin/eventstage/add", methods=["GET", "POST"])
def addeventstage():
    stagename=request.form.get('StageName')
    eventid=request.form.get('EventID')
    location=request.form.get('Location')
    stagedate=request.form.get('StageDate')
    qualifying=request.form.get('Qualifying')
    pointstoqualify=request.form.get('PointsToQualify')
    connection=getCursor()
    connection.execute("INSERT INTO event_stage (StageName, EventID, Location, StageDate, Qualifying, PointsToQualify) VALUES (%s, %s, %s, %s, %s, %s);", (stagename, eventid, location, stagedate, qualifying, pointstoqualify),)
    
    connection=getCursor()
    sql = "SELECT * FROM events INNER JOIN event_stage on event_stage.EventID=events.EventID WHERE events.EventID=%s;"
    connection.execute(sql, (eventid,))
    stageList=connection.fetchall()
    return render_template("addeventstage.html",stagelist=stageList)

@app.route("/admin/addscores", methods=["GET", "POST"])
def addscores():
    connection=getCursor()
    sql_event="SELECT * FROM events;"
    connection.execute(sql_event)
    eventList=connection.fetchall()
    #print(eventList)
    return render_template("addscores_event.html", eventlist=eventList)

@app.route("/admin/addscores/event",methods=["GET","POST"] )
def chooseevent():
    eventID=request.form.get('EventID')
    connection=getCursor()
    sql_stage="SELECT * FROM event_stage WHERE EventID=%s;"
    connection.execute(sql_stage,(eventID,))
    stageList=connection.fetchall()
    if len(stageList) == 0:
        return render_template ("addscores_noeventstage.html")
    else:
        return render_template ("addscores_eventstage.html", stagelist=stageList)

@app.route("/admin/addscores/stageid", methods=["POST"])
def choosestage():
    stageID=request.form.get('StageID')
    connection=getCursor()
    sql_member="SELECT MemberID FROM members;"
    connection.execute(sql_member)
    memberID=connection.fetchall()
    sql_stage="SELECT StageName FROM event_stage WHERE StageID=%s;"
    connection.execute(sql_stage, (stageID, ))
    stageName=connection.fetchone()
    #print(stageName)
    return render_template("addscores_update.html", stageid=stageID, memberid=memberID, stagename=stageName)

@app.route("/admin/addscores/update", methods=["POST"])
def score():
    stageID=request.form.get('StageID')
    memberID=request.form.get('MemberID')
    PointsScored=request.form.get('PointsScored')
    Position=request.form.get('Position')
    connection=getCursor()
    connection.execute("INSERT INTO event_stage_results (StageID, MemberID, PointsScored, Position) VALUES (%s, %s, %s, %s);",(stageID, memberID, PointsScored, Position),)
    sql="SELECT * FROM event_stage_results WHERE StageID=%s;"
    connection.execute(sql,(stageID,))
    Results=connection.fetchall()
    return render_template ("addscores_display.html", results=Results)


@app.route("/admin/reports", methods=["GET","POST"])
def reports():

    return render_template("reports.html")

@app.route("/admin/report/type", methods=["POST"])
def reporttype():
    Type=request.form.get('type')
    connection=getCursor()
    sql_member="SELECT * FROM members JOIN teams ON teams.TeamID=members.TeamID ORDER BY members.LastName, members.FirstName;;"
    connection.execute(sql_member)
    memberList=connection.fetchall()
    sql_team="SELECT * FROM teams;"
    connection.execute(sql_team)
    teamList=connection.fetchall()
    sql_medal="""SELECT members.MemberID, members.FirstName, members.LastName, event_stage_results.Position 
              FROM event_stage_results JOIN members ON members.MemberID=event_stage_results.memberID;"""
    connection.execute(sql_medal)
    medalList=connection.fetchall()
    gold=0
    sliver=0
    bronze=0
    for numberoftimes in range(0, len(medalList), 1):
            if medalList[numberoftimes][3]==1:
                gold=gold+1
            elif medalList[numberoftimes][3]==2:
                sliver=sliver+1
            elif medalList[numberoftimes][3]==3:
                bronze=bronze+1        

    if Type == "medal":
        return render_template("reports_medal.html", medallist=medalList, gold=gold, sliver=sliver, bronze=bronze)
    elif Type == "member":
        return render_template("reports_member.html", teamlist=teamList, memberlist=memberList)


