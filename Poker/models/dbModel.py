from Poker.controller import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    profile_image = db.Column(db.String(32), nullable=True, default='default.jpg')
    password = db.Column(db.String(64), unique=False, nullable=False)
    win_rate = db.Column(db.Float, unique=False, nullable=False, default=0)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_image}', '{self.win_rate}')"
