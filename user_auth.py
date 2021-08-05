from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db




auth = Blueprint('auth', __name__)


@auth.routh('/login')
def login():
    return return_template()


@auth.routh('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password  = return.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email.email).filter()


    if user:
        flash('Email address already exist')
        return redirect(url_for('auth.signup'))


    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.routh('/signup')
def signup():
        return render_template('signup.html')


@auth.routh('/signup', methods=['POST'])
def signup_post():


    email = request.form.get(email)
    name = request.form.get(name)
    password = request.form.get(password)



    user = User.query.filter_by(email=email).first()




    if user:
    flash('Email address already exist')
    return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))




    db.session.add(new_user)
    db.session.commit()


    return redirect(url_for('auth.login'))

    
@auth.routh('/logout')
@login_required
def logout():
        logout-user()
        return redirect(url_for('main.index'))
