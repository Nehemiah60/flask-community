from datetime import datetime, timedelta
from flask_community import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(100), index=True, unique=True)
    email         = db.Column(db.String(100), index=True, unique=True)
    password      = db.Column(db.String(100))
    joined_date   = db.Column(db.DateTime, default=datetime.utcnow)
    post          = db.relationship('Post', backref='author', lazy=True)
    Comment       = db.relationship('Comment', backref='author', lazy=True)

    def __repr__(self):
        return f"User( '{self.username}', '{self.email}')"

class Post(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(100), nullable=False)
    content       = db.Column(db.Text, nullable=False)
    date_created  = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id       = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    comment       = db.relationship('Comment', backref='comment', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_created}')"

class Comment(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    content       = db.Column(db.Text, nullable=False)
    date_created  = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id       = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    post_id       = db.Column(db.Integer, db.ForeignKey(Post.id), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content}')"