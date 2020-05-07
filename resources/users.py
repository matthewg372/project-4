import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users')

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