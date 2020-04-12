from flask_login import UserMixin

from Poker.controller import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    profile_image = db.Column(db.String(32), unique=False, nullable=True, default='default.jpg')
    password = db.Column(db.String(64), unique=False, nullable=False)
    win_rate = db.Column(db.Float, unique=False, nullable=False, default=0)
    savings = db.Column(db.Integer, unique=False, nullable=False, default=0)
    games_played = db.Column(db.Integer, unique=False, nullable=False, default=0)

    def __repr__(self):
        return f"User('" \
               f"{self.username}', '{self.email}', '{self.savings}', '{self.profile_image}', '{self.win_rate}', " \
               f"'{self.games_played}')"
