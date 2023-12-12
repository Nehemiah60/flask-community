
from flask_community import app, bcrypt, db
from flask import render_template
from flask_community.forms import RegisterUserForm
from flask_community.models import User

@app.route('/')
def home():
    return render_template('home.html')

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