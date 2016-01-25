from flask import render_template, g, url_for, request, redirect
from app import app, db
from .models import User, Answer
from .forms import QuestionForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():


    # Load user ID from cookie
    user_id = request.cookies.get('user_id')

    # If there is no user ID in cookie, create user
    if user_id is None:
        # Add user to database
        user = User()
        db.session.add(user)
        db.session.commit()

        # Add user_id into cookie
        response = redirect(url_for('index'))
        response.set_cookie('user_id', str(user.id))
        return response

    # Load user credentials from db by ID
    user = User.query.filter_by(id=user_id).first()
    print('user_id = %s' % user_id)
    print('user.id = %s' % user.id)

    # Question form
    form = QuestionForm()

    if request.method == 'POST':
        print('POST form option was ' + form.options.data)
        user.answer_id = form.options.data
        db.session.add(user)
        db.session.commit()
        print('POSTED answer id: %s' % user.answer_id)
        return redirect(url_for('index'))

    if user.answer_id is None:
        return render_template('index.html', question=True, form=form)

    return render_template('index.html', results=True, answer=user.answer_id)
