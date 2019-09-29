# 1. import Flask
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

#Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to weather app!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/2012-04-23<br/>"
        f"/api/v1.0/2012-04-23/2012-05-16")

#Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precip():
    year_ago = dt.date(2016, 8, 23)
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= year_ago).\
    order_by(Measurement.date).all()
    session.close()
    json_precip = dict(results)
    print("Server received request for 'precipitation' page...")
    return jsonify(json_precip)

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'stations' page...")
    session = Session(engine)
    results = session.query(Station.name).all()
    session.close()
    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' page...")
    year_ago = dt.date(2016, 8, 23)
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= year_ago).\
    order_by(Measurement.date).all()
    session.close()
    return jsonify(results)

@app.route("/api/v1.0/<start>")
def start_temp(start):
    print("Server received request for 'start_temp' page...")
    """TMIN, TAVG, and TMAX for a list of dates.
    Args:
        start_date (string): A date string in the format %Y-%m-%d
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()
    temps =  list(np.ravel(results))
    return jsonify(temps)

@app.route("/api/v1.0/<start>/<end>")
def start_end_temps(start, end):
    print("Server received request for 'start_end_temp' page...")
    """TMIN, TAVG, and TMAX for a list of dates.
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    temps =  list(np.ravel(results))
    return jsonify(temps)

if __name__ == "__main__":
    app.run(debug=True)