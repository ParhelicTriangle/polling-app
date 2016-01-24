from flask.ext.wtf import Form
from wtforms import SelectField

class QuestionForm(Form):
    options = SelectField('Label', choices=[
                                            ('apples','apples'),
                                            ('bananas', 'bananas'),
                                            ('oranges', 'oranges')
                                            ])
