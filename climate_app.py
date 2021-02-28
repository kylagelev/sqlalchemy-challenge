import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime, timedelta

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
    print("Climate App")
    return (f"Welcome to the Climate App.<br/><br/>"
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

    session.close()

    return jsonify(prcp_dates)

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    station = Base.classes.station
    results = session.query(station.station).all()

    station_list = []
    for station in results:
        station_name = station
        station_list.append(station_name)
    
    session.close()
        
    return jsonify(station_list)

@app.route('/api/v1.0/tobs')
def tob():
    session = Session(engine)
    max_station = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).\
        order_by(func.count(measurement.station).desc()).limit(1)[0][0]
    temp_max_station = session.query(measurement.date, measurement.tobs).filter(measurement.station == max_station).all()
    max_date = session.query(measurement.date, measurement.tobs).filter(measurement.station == max_station).\
        order_by((measurement.date).desc()).limit(1)[0][0]
    
    tempdate_list = []
    for date, temp in temp_max_station: 
        date_temp = date
        temperature = temp
        tempdate_list.append(date_temp, temperature)

    session.close()

    return jsonify(tempdate_list, max_date)

@app.route('/api/v1.0/<start>') 
def start(start):
    session = Session(engine)

    temp_start = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start).all()

    temp_stats = []
    for min_temp, max_temp, avg_temp in temp_start:
        tobs_dict = {}
        tobs_dict['min'] = min_temp
        tobs_dict['max'] = max_temp 
        tobs_dict['avg'] = avg_temp
        temp_stats.append(tobs_dict)

    session.close()

    return jsonify(temp_stats)

@app.route('/api/v1.0/<start>/<end>')
def startend(start, end):
    session = Session(engine)

    temp_end_start = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()

    temp_start_end_stats = []
    for min_temp, max_temp, avg_temp in temp_end_start:
        tobs_dict = {}
        tobs_dict['min'] = min_temp
        tobs_dict['max'] = max_temp 
        tobs_dict['avg'] = avg_temp
        temp_start_end_stats.append(tobs_dict)

    session.close()

    return jsonify(temp_start_end_stats)


if __name__ == '__main__':
    app.run(debug=True)