from datetime import datetime, timedelta
from flask_community import db

class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(100), index=True, unique=True)
    email         = db.Column(db.String(100), index=True, unique=True)
    password      = db.Column(db.String(100))
    joined_date   = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User( '{self.username}', '{self.email}')"