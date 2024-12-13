# import dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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