import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

profiles = Blueprint('profiles', 'profiles')

@profiles.route('/', methods=['POST'])
def create_profile():
	payload = request.get_json()
	new_profile = models.Profile.create(
		user=current_user.id,
		images=payload['images'],
		first_Name=payload['firstName'],
		Last_Name=payload['lastName'],
		days_Sober=payload['daysSober'],
		Age=payload['age'],
		Sponser=payload['sponsor'],
	)
	profile_dict = model_to_dict(new_profile)
	profile_dict['user'].pop('password')
	return jsonify(
		data=profile_dict,
		message="successfully created profile",
		status=200
	),200