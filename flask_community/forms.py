from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                    SubmitField, TextAreaField)
from wtforms.validators import (DataRequired, Email, 
                                EqualTo, Length, ValidationError)
from flask_community.models import User

class RegisterUserForm(FlaskForm):
    username         = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email            = StringField('Email', validators=[DataRequired(), Email()])
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password', message='Password do not match') ])
    submit           = SubmitField('Signup')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Try another')
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Try another')

class LoginForm(FlaskForm):
    email            = StringField('Email', validators=[DataRequired(), Email()])
    password         = PasswordField('Password', validators=[DataRequired()])
    submit           = SubmitField('Signup')

class PostForm(FlaskForm):
    title            = StringField('Title', validators=[DataRequired()])
    content          = TextAreaField('Content', validators=[DataRequired()])
    submit           = SubmitField('Post')

class UpdatePostForm(FlaskForm):
    title            = StringField('Title', validators=[DataRequired()])
    content          = TextAreaField('Content', validators=[DataRequired()])
    submit           = SubmitField('Update')

