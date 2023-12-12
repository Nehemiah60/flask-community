from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nehecode@localhost:5432/comm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY']= '0f3991c35406b3dd6989'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt  = Bcrypt(app)
login_manager = LoginManager(app)

import flask_community.views
import flask_community.models