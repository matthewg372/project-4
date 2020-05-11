import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

profiles = Blueprint('profiles', 'profiles')


@profiles.route('/user/<id>', methods=['GET'])
@login_required
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
@login_required
def all_profiles():
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
@login_required
def create_profile():
	payload = request.get_json()
	new_profile = models.Profile.create(
		user=current_user.id,
		images=payload['images'],
		first_name=payload['first_name'],
		last_name=payload['last_name'],
		days_sober=payload['days_sober'],
		date_of_birth=payload['date_of_birth'],
		sponsor=payload['sponsor'],
	)
	profile_dict = model_to_dict(new_profile)
	profile_dict['user'].pop('password')
	return jsonify(
		data=profile_dict,
		message="successfully created profile",
		status=200
	),200


@profiles.route('/<id>', methods=['DELETE'])
@login_required
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
@login_required
def update_profile(id):
	payload = request.get_json()
	profile_to_update = models.Profile.get_by_id(id)
	if current_user.id == profile_to_update.user.id:
		if 'images' in payload:
			profile_to_update.images=payload['images']
		if 'first_name' in payload:
			profile_to_update.first_name=payload['first_name']
		if 'last_name' in payload:
			profile_to_update.last_name=payload['last_name']
		if 'days_sober' in payload:
			profile_to_update.days_sober=payload['days_sober']
		if 'date_of_birth' in payload:
			profile_to_update.date_of_birth=payload['date_of_birth']
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









