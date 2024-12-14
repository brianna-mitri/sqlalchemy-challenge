# import dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

# ------------------------------
# Database Setup
#-------------------------------

# create engine to database
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect existing database into new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link from python to database
session = Session(engine)


# ------------------------------
# Flask Setup
#-------------------------------
app = Flask(__name__)


# ------------------------------
# Flask Routes & Queries
#-------------------------------

# define function to get year ago date
def get_year_ago_date(session):
    
    # find the most recent data in the dataset
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d').date()

    # get the date from 12 months prior
    return recent_date - dt.timedelta(days=365)

# homepage route (list all available routes)
@app.route('/')
def home():
    return (
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end><br/>'
    )

# precipitation route (returns date and precipitation for last year in db)
@app.route('/api/v1.0/precipitation')
def precipitation():

    # get year ago date
    year_ago_date = get_year_ago_date(session)

    # perform query to get the previous 12 months of precipitation data (date and precipitation scores)
    prcp_data_year_ago = (session.query(Measurement.date, Measurement.prcp)
                          .filter(Measurement.date >= year_ago_date)
                          .all())
    
    # convert query results into a dictionary
    prcp_dict = {date: prcp for date, prcp in prcp_data_year_ago}

    # return the JSON representation of precipitation data
    return jsonify(prcp_dict)

# stations route (return stations' data)
@app.route('/api/v1.0/stations')
def stations():

    # query list of stations
    stations = (session.query(
                Station.station, 
                Station.name, 
                Station.latitude, 
                Station.longitude, 
                Station.elevation)
                .all())
    
    # convert result into list of dictionaries
    station_info = []
    for id, name, lat, lon, elev in stations:
        station_dict = {
            'station': id,
            'name': name,
            'latitude': lat,
            'longitude': lon,
            'elevation': elev
        }
        station_info.append(station_dict)

    # return JSON list
    return jsonify(station_info)

# tobs route (return dates and temp of most active station for recent 12 months)
@app.route('/api/v1.0/tobs')
def tobs():

    # query to find the most active stations (most rows)
    active_stations = (session.query(Measurement.station, func.count(Measurement.station))
                       .group_by(Measurement.station)
                       .order_by(func.count(Measurement.station).desc())
                       .all())
    
    # get the most active station
    most_active_station = active_stations[0][0]

    # get year ago date
    year_ago_date = get_year_ago_date(session)

    # query the last 12 months of temperature observation data for this station
    temp_data_year_ago = (session.query(Measurement.date, Measurement.tobs)
                          .filter(Measurement.station == most_active_station)
                          .filter(Measurement.date >= year_ago_date)
                          .all())
    
    # convert query results into a dictionary
    temp_dict = {date: tobs for date, tobs in temp_data_year_ago}

    # return json list
    return jsonify(temp_dict)

# start route

# start/end route


# run local server with the app
if __name__ == '__main__':
    app.run(debug=True)