from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    moods = db.relationship('Mood', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.name)

class Mood(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(32))
	category = db.Column(db.String(16))
	description = db.Column(db.String(256))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Mood %r>' % (self)


