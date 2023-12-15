
from datetime import datetime
from flask_community import app, bcrypt, db, login_manager
from flask import render_template, url_for, redirect, flash
from flask_community.forms import RegisterUserForm, LoginForm
from flask_community.models import User, Post
from flask_login import login_user, login_required, current_user, logout_user


@app.route('/home')
@login_required
def home():
    posts = Post.query.all()
    now = datetime.utcnow()
    return render_template('home.html', posts=posts, now=now)

@app.route('/register', methods=['POST', 'GET'])
def register_user():
    form = RegisterUserForm()
    if form.validate_on_submit():
       
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user            = User(
                                    username  = form.username.data,
                                    email     = form.email.data,
                                    password  = hashed_password
                                    )
        try:
            db.session.add(user)
            db.session.commit()    
        except:
            db.session.rollback()
        finally:
            db.session.close()
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Login Attempt Failed. Check Email and Password', 'danger')  
        except:
            flash('Unexpected error occured')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.errorhandler(401)
def unauthorized(error):
    flash('You mush be logged in to access the page. Login here', 'danger')
    return redirect(url_for('login'))