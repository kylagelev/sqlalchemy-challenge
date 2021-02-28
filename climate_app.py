import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    print("Welcome")
    return (f"Welcome to the Climate App."
            "Available Routes:<br/>" 
            "/api/v1.0/precipitation<br/>"
            "/api/v1.0/stations<br/>"
            "/api/v1.0/tobs<br/>"
            "/api/v1.0/<start><br/>"
            "/api/v1.0/<start>/<end><br/>")




@app.route('/api/v1.0/precipitation')
def precipitation():

    return

@app.route('/api/v1.0/stations')
def stations():

    return

@app.route('/api/v1.0/tobs')
def tob():

    return

@app.route('/api/v1.0/<start>') 
def start():


    return

@app.route('/api/v1.0/<start>/<end>')
def startend():

    return