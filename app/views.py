from flask import render_template, g
from app import app, db
from .models import User, Answer
from .forms import QuestionForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = QuestionForm()

    if form.validate_on_submit():
        print(form.options.data)
    else:
        print(form.errors)

    return render_template('index.html', form=form)
