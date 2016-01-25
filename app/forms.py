from flask.ext.wtf import Form
from wtforms import SelectField
from .models import Answer

class QuestionForm(Form):
    choices = []
    answers = Answer.query.all()
    for answer in answers:
        answer = (answer.id, answer.name)
        choices.append(answer)
        
    options = SelectField('Label', choices=choices)
