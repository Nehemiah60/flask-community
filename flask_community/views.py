
from datetime import datetime
from flask_community import app, bcrypt, db, login_manager
from flask import render_template, url_for, redirect, flash, abort, request, jsonify
from flask_community.forms import (RegisterUserForm, LoginForm, PostForm, 
                                    CommentForm,UpdatePostForm)
from flask_community.models import User, Post, Comment
from flask_login import login_user, login_required, current_user, logout_user


@app.route('/home')
@login_required
def home():
    form = UpdatePostForm()
    comment_form = CommentForm()
    posts = Post.query.all()
    #Get comments related to a specific post
    comments_count = {post.id: Comment.query.filter_by(post_id=post.id).count() for post in posts}
    now = datetime.utcnow()
    return render_template('home.html', posts=posts, now=now, 
                            form=form, comment_form=comment_form,
                            comments_count=comments_count)

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

@app.route('/post/new', methods=['POST', 'GET'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        try:
            post = Post( title = form.title.data,
                         content = form.content.data,
                         comment_author  = current_user
            )
            db.session.add(post)
            db.session.commit()
            flash('Post created successfully', 'success')
            return redirect(url_for('home'))
        except:
            flash('Fail!')
    return render_template('create_post.html', form=form)

#Delete Post...A user is the only one cable to delete a post
@app.route('/delete_post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    try: 
        post = Post.query.get_or_404(post_id)
        if post.author != current_user:
            abort(403)
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted', 'success')
    except:
        db.session.rollback
    finally:
        db.session.close()
        return redirect(url_for('home'))
     

#Update Post
@app.route('/post/<int:post_id>/update_post', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    form = UpdatePostForm()
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if form.validate_on_submit():
        try:
            post.title   = form.title.data
            post.content = form.content.data
            db.session.commit()
            flash('Your Post Updated Successfully', 'success')
            return redirect(url_for('home'))
        except:
            db.session.rollback()
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('home.html', form=form)

@app.route('/add_comments/<int:post_id>', methods=['GET', 'POST'])
@login_required
def add_comment(post_id):
    post        = Post.query.get_or_404(post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        try:
            comment = Comment(
                content  = comment_form.content.data,
                comment_author   = current_user,
                post          = post
            )
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('home'))
        except:
            db.session.rollback()    
    return render_template('home.html', comment_form=comment_form)


#POPULATING THE FORM WITH DATA DURING UPDATES
@app.route('/api/get_post/<int:post_id>', methods=['GET', 'POST'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({'title': post.title, 'content': post.content})


@app.errorhandler(401)
def unauthorized(error):
    flash('You mush be logged in to access the page. Login here', 'danger')
    return redirect(url_for('login'))