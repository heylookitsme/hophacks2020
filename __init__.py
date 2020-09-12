from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user
from __init__ import db
import time

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(1000))

	sanitizer = db.Column(db.Integer)
	cloth = db.Column(db.Integer)
	gloves = db.Column(db.Integer)
	surgical = db.Column(db.Integer)


um = Blueprint('um',  __name__)

@um.route('/projects/hophacks2020/login')
def login():
	return render_template(login.html)

@um.route('/projects/hophacks2020/login', methods=['POST']) 
def login_submitted():
	email = request.form.get('email')
	password = request.form.get('password')

	user = User.query.filter_by(email=email).first()

	if not user or not check_password_hash(user.password, password):
		return redirect(url_for('login'))

	login_user(user)
	return redirect(url_for('user_pages.supplies'))

@um.route('/projects/hophacks2020/register')
def register():
	return render_template('register.html')

@um.route('/projects/hophacks2020/register', methods=['POST'])
def register_submitted():
	email = request.form.get('email')
	name = request.form.get('name')
	password = request.form.get('password')

	user = User.query.filter_by(email=email).first()

	if user:
		return redirect(url_for('login'))

	new_user = User(id = int(time.time()), email=email, name=name, password=generate_password_hash(password, method='sha256'), sanitizer = 0, cloth = 0, gloves = 0, surgical = 0)

	db.session.add(new_user)
	db.session.commit()
	
	return redirect(url_for('login')) 

@um.route('/projects/hophacks2020/logout')
def logout():
	logout_user()
	return redirect('login')
