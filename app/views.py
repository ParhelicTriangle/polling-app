from flask import render_template, flash, redirect, url_for, request, g
from app import app, db
from .models import User, Answer

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
