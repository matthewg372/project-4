import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user

users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])

@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()
	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify(
			data={},
			message=f"user with {payload['email']}",
			status=401
		),401
	except models.DoesNotExist:
		pw_hash = generate_password_hash(payload['password'])
		created_user = models.User.create(
			username=payload['username'],
			email=payload['email'],
			password=pw_hash
		)
		created_user_dict = model_to_dict(created_user)
		created_user_dict.pop('password')
		return jsonify(
			data=created_user_dict,
			message=f"succesfully registered {created_user_dict['email']}",
			status=201
		),201

@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()
	try:
		user = models.User.get(models.User.email == payload['email'])
		user_dict = model_to_dict(user)
		password_is_good = check_password_hash(user_dict['password'], payload['password'])
		if(password_is_good):
			login_user(user)
			user_dict.pop('password')
			return jsonify(
				data=user_dict,
				message=f"succesfully logged in {user_dict['email']}",
				status=200
			), 200
		else:
			return jsonify(
				data={},
				message="Email or Password is incorrect",
				status=401
			), 401
	except models.DoesNotExist:
		return jsonify(
			data={},
			message="Email or Password is incorrect",
			status=401
		),401


@users.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return jsonify(
		data={},
		message="succesfully logged out",
		status=200
	), 200











