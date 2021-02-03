import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
    return app

INSTANCE = None
def app():
    global INSTANCE
    if INSTANCE == None :
        INSTANCE = create_app()
    return INSTANCE
    