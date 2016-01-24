import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir

app = Flask(__name__)

# Use config.py as application configuration file
app.config.from_object('config')

# Database setup
db = SQLAlchemy(app)

# Can only be done after app and db have been initialised
from app import views, models
