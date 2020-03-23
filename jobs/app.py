import flask
from flask import render_template, Flask, g
import sqlite3

PATH = 'db\jobs.sqlite'
app = flask.Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection, g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.row
    return connection
    
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template("index.html")
