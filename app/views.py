from flask import render_template, g, url_for, request, redirect
from app import app, db
from .models import User, Answer
from .forms import QuestionForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # Check if question has been answered, if so, show results page
    answered = request.cookies.get('answered')
    if answered == 'yes':
        return redirect(url_for('results'))

    form = QuestionForm()
    if form.validate_on_submit():
        print(form.options.data)
        response = redirect(url_for('results'))
        response.set_cookie('answered', 'yes')
        return response
    else:
        print(form.errors)

    return render_template('index.html', form=form)


@app.route('/results')
def results():
    return render_template('results.html')
