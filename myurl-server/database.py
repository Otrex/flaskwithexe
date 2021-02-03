from app import app
from flask_sqlalchemy import SQLAlchemy

DBINSTANCE = None

def db():
	global DBINSTANCE, app
	if DBINSTANCE == None:
		app = app()
		DBINSTANCE = SQLAlchemy(app)
	return DBINSTANCE