from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'b09c4250f8465dd0cd538b5082f909cf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from Poker.controller import routes
