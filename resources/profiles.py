import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

profiles = Blueprint('profiles', 'profiles')


@profiles.route('/user/<id>', methods=['GET'])
def user_products_index(id):
	user_profile = models.User.get_by_id(id)
	current_user_profile_dicts = [model_to_dict(product) for product in user_profile.profiles]
	print(current_user_profile_dicts)
	for profile_dict in current_user_profile_dicts:
		profile_dict['user'].pop('password')
	return jsonify(
		data= current_user_profile_dicts,
		message= f"Successfully found {len(current_user_profile_dicts)} profile",
		status= 200
	), 200

@profiles.route('/all', methods=['GET'])
def all_profiles():
	print('working')
	profiles = models.Profile.select()
	profiles_dicts = [model_to_dict(profile) for profile in profiles]
	for profile_dict in profiles_dicts:
		profile_dict['user'].pop('password')
	return jsonify(
		data=profiles_dicts,
		message="successfully showed all profiles",
		status=200
	),200

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
@profiles.route('/<id>', methods=['DELETE'])
def delete_profile(id):
	profile_to_delete = models.Profile.get_by_id(id)
	if current_user.id == profile_to_delete.user.id:
		delete_query = models.Profile.delete().where(models.Profile.id == id)
		delete_query.execute()
		print('deleted')
		return jsonify(
			data={},
			message=f"successfully deleted {id}",
			status=200
		), 200
	else:
		return jsonfiy(
			data={},
			message="you must be logged in",
			status=403
			),403
@profiles.route('/<id>', methods=['PUT'])
def update_profile(id):
	payload = request.get_json()
	profile_to_update = models.Profile.get_by_id(id)
	print("--------",profile_to_update.first_Name)
	if current_user.id == profile_to_update.user.id:
		if 'images' in payload:
			profile_to_update.images=payload['images']
		if 'firstName' in payload:
			profile_to_update.first_Name=payload['firstName']
		if 'lastName' in payload:
			profile_to_update.Last_Name=payload['lastName']
		if 'daysSober' in payload:
			profile_to_update.days_Sober=payload['daysSober']
		if 'Age' in payload:
			profile_to_update.Age=payload['Age']
		if 'sponsor' in payload:
			profile_to_update.sponsor=payload['sponsor']
		profile_to_update.save()
		profile_updated_dict = model_to_dict(profile_to_update)
		profile_updated_dict['user'].pop('password')
		return jsonify(
			data=profile_updated_dict,
			message=f"successfully updated {id}",
			status=200
		),200
	else:
		return jsonify(
			data={},
			message="you must be logged in to update",
			status=403
		), 403









