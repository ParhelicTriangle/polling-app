from app import db

class User(db.Model):
    # Define table columns
    id = db.Column(db.Integer, primary_key=True)

    # Define relationships
    # Foreign key of one-to-many relationship is defined on 'many' side
    # Parent table elements are referenced using 'backref' in db relationship
    # E.g. if backref=answer, answer name can be accessed using user.answer.name
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))

    def has_user_answered(self):
        if self.answer_id is None:
            return False
        return True

class Answer(db.Model):
    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)

    # Relationship is defined on the 'one' side of the one to many relationship
    users = db.relationship('User', backref='answer', lazy='dynamic')
