from app import db, models
import csv

with open('users_hack.csv', 'rb') as csvfile:
	file_reader = csv.reader(csvfile, delimiter = ',', quotechar='"')
	for row in file_reader:
		newuser = models.User(firstname = row[0], lastname = row[1], username = row[2])
		db.session.add(newuser)

db.session.commit()

print 'done!'