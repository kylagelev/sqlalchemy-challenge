import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

database_path = 'Resources/hawaii.sqlite'
engine = create_engine(f'sqlite:///{database_path}')
Base = automap_base()
Base.prepare(engine, reflect=True)
measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)

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
    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).all()

    prcp_dates = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_dates.append(prcp_dict)
    return jsonify(prcp_dates)

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)

    return

@app.route('/api/v1.0/tobs')
def tob():
    session = Session(engine)

    return

@app.route('/api/v1.0/<start>') 
def start():
    session = Session(engine)


    return

@app.route('/api/v1.0/<start>/<end>')
def startend():
    session = Session(engine)

    return