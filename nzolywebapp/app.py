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
    sql = "SELECT members.FirstName, members.LastName, members.MemberID, teams.TeamName, members.City, members.Birthdate\
          FROM members\
          INNER JOIN teams\
          ON members.TeamID = teams.TeamID;"
    connection.execute(sql)
    memberList = connection.fetchall()
    #print(memberList)
    return render_template("memberlist.html", memberlist = memberList)    

@app.route("/listmembers/athlete/detail", methods=['GET', 'POST'])
def athlete_detail():
    memberid = request.form.get('id')
    #memberid = int(memberID)
    #print(memberid)
    connection = getCursor()
    sql="""SELECT members.FirstName, members.LastName, members.MemberID, events.EventName, event_stage.StageDate, event_stage.StageName, event_stage.Location, event_stage.Qualifying, event_stage_results.Position
            FROM events JOIN event_stage on events.EventID=event_stage.EventID 
            JOIN event_stage_results on event_stage.StageID=event_stage_results.StageID
            JOIN members on event_stage_results.MemberID=members.MemberID WHERE members.MemberID=%s;"""
    connection.execute(sql, (memberid,))
    Details = connection.fetchall()
    #print(Details)
    return render_template("athlete.html", details=Details)

@app.route("/listevents")
def listevents():
    connection = getCursor()
    connection.execute("SELECT * FROM events;")
    eventList = connection.fetchall()
    return render_template("eventlist.html", eventlist = eventList)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/search/result_member", methods=["POST"])
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

@app.route("/search/result_event", methods=["POST"])
def searchresult_event():
    searchterm = request.form.get('eventsearch')
    #print(searchterm)
    likesearchterm = f'%{searchterm}%'
    connection = getCursor()
    connection.execute("SELECT * FROM events WHERE EventName LIKE %s;", (likesearchterm,))
    eventList = connection.fetchall()
    return render_template("search.html", eventlist=eventList) 

@app.route("/addeditmember")
def addeditmember():
    connection = getCursor()
    sql = "SELECT * FROM members;"
    connection.execute(sql)
    memberList = connection.fetchall()
    return render_template("addeditmember.html", memberlist=memberList)

@app.route("/member/add", methods=["POST"])
def addmembers():
    memberid=request.form.get('MemberID')
    teamid=request.form.get('TeamID')
    firstname=request.form.get('FirstName')
    lastname=request.form.get('LastName')
    city=request.form.get('City')
    birthdate=request.form.get('Birthdate')

    connection = getCursor()
    connection.execute("INSERT INTO members (MemberID, TeamID, FirstName, LastName, City, Birthdate) VALUES (%s, %s, %s, %s, %s, %s);", (memberid, teamid, firstname, lastname, city, str(birthdate),))
    
    return redirect ("/addeditmember")

@app.route("/member/edit/<memberid>")
def editmember(memberid):
    #print(memberid)
    connection=getCursor()
    sql = "SELECT * FROM members WHERE memberid=%s;"
    connection.execute(sql, (memberid,))
    memberEditting=connection.fetchone()
    return render_template ("editmember.html", membereditting=memberEditting)

@app.route("/updatemember",  methods=["POST"])
def updatemember():
    memberid=request.form.get('MemberID')
    teamid=request.form.get('TeamID')
    firstname=request.form.get('FirstName')
    lastname=request.form.get('LastName')
    city=request.form.get('City')
    birthdate=request.form.get('Birthdate')

    connection = getCursor()
    connection.execute("UPDATE members SET MemberID=%s, TeamID=%s, FirstName=%s, LastName=%s, City=%s, Birthdate=%s WHERE MemberID=%s;", (memberid, teamid, firstname, lastname, city, str(birthdate), memberid, ))

    return redirect ("/addeditmember")



@app.route("/addevents")
def addevents():
    return render_template("addevents.html")

@app.route("/addscores")
def addscores():
    return render_template("addscores.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

