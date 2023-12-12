from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                    SubmitField)
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
            raise ValidationError('A user with that username already exists. Choose a different username')
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('A user with that email already exists. Choose a different email')