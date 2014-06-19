# -*- coding: utf-8 -*-
#Section 1: Importing tools
from app import app, db
from flask import render_template
from models import Member, Event


#Section 2: Views
@app.route('/', methods = ['GET', 'POST'])
def index():
	members = Member.query.all()
	return render_template('index.html', members = members)

@app.route('/events', methods = ['GET', 'POST'])
def events():
	events = Event.query.all()
	return render_template('events.html', events = events)

#Status Update:
	#Have been able to do:
		#Launched the flask app
		#Create a database
	#Was Stuck:
		#After running the dbcreate python script and no errors given, my tables are not showing up. But noticed that it was creating tabels in my last database. I deleted the config file then created a new one. 
		