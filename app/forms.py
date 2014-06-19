from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField #I am trying to import this but it is telling me that it can't import. I would like to get
from wtforms.validators import Required 

class NewUserForm(Form):
	firstname = TextField('firstname')
	lastname = TextField('lastname')
	username = TextField('username', validators= [Required(message = 'username, please!')])

class NewPostForm(Form):
	title = TextField ('title')
	author = TextField ('author')
	content = TextAreaField ('content')
	