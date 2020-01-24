import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# db location
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect db onto classes
Base = automap_base()

Base.prepare(engine, reflect=True)

# Reference tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# session link python to db
session = Session(engine)

# create flask application named app
app = Flask(__name__)

# homepage/welcome route/root
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# precipitation page
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    Measurement = Base.classes.measurement
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    session.close()
    return jsonify(precip)

# Station page
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    session.close()
    return jsonify(stations)

# Temperature page
@app.route("/api/v1.0/tobs")
def temp_monthly():
    session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    session.close()
    return jsonify(temps)

# Temp data range page
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start, end):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    session.close()
    return jsonify(temps)
    # Measurement = Base.classes.measurement
    # sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # if not end:
	# results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    # temps = list(np.ravel(results))
    # return jsonify(results)
    #     results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    #     temps = list(np.ravel(results))
    # session.close()
    # return jsonify(temps)