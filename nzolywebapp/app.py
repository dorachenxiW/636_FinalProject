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

@app.route("/listmembers/athlete/<name>", methods=["GET"])
def athlete(name):
    connection=getCursor()
    print(name)
    sql_previous = "SELECT event_stage.StageDate, event_stage.StageName, event_stage.Location, event_stage.Qualifying, event_stage_results.Position\
          FROM event_stage inner join event_stage_results ON event_stage.StageID = event_stage_results.StageID\
            WHERE name = s%, (name,);"
    connection.execute(sql_previous)
    previousevents = connection.fetchall()
    return render_template("athlete.html", name=name, previousevents=previousevents)

@app.route("/listevents")
def listevents():
    connection = getCursor()
    connection.execute("SELECT * FROM events;")
    eventList = connection.fetchall()
    return render_template("eventlist.html", eventlist = eventList)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/addmembers")
def addmembers():
    return render_template("addmembers.html")

@app.route("/addevents")
def addevents():
    return render_template("addevents.html")

@app.route("/addscores")
def addscores():
    return render_template("addscores.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

