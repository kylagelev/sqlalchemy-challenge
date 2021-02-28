from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    print("Welcome")
    return ("Welcome to the Climate App."
    Available Routes:


@app.route('/api/v1.0/precipitation')
def precipitation():

@app.route('/api/v1.0/stations')
def stations():

@app.route('/api/v1.0/tobs')
def tob():

@app.route('/api/v1.0/<start>') 
def start():

@app.route('/api/v1.0/<start>/<end>')
def start/end():