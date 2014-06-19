from app import db

class Member(db.Model): #When you are making a new class you capitialize the title ex. class User()
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	email = db.Column(db.String(120), unique =True)
	password = db.Column(db.String(100))

class Event(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String (100))
	date = db.Column(db.DateTime)
	city = db.Column(db.String(100))
	count = db.Column(db.Integer) #when you are refering to a class, it is lowercase
	event_id = db.Column(db.Integer, db.ForeignKey('member.id'))



