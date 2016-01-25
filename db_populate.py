#!env/bin/python
from app import app, db, models

options = ['apple', 'banana', 'orange']

for option in options:
    a = models.Answer(name=option)
    db.session.add(a)
    db.session.commit()
