import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/liberation'

CSRF_ENABLED = True #This is to prevent CSRF attacks - so that all of our data comes from our forms
SECRET_KEY = 'big-secret'