from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'b09c4250f8465dd0cd538b5082f909cf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../models/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
socket = SocketIO(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)


from Poker.controller import routes
