import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

meetings = Blueprint('meetings', 'meetings')

@meetings.route('/all', methods=['GET'])
def all_profiles():
	meetings = models.Meeting.select()
	meetings_dicts = [model_to_dict(meeting) for meeting in meetings]
	for meeting_dict in meetings_dicts:
		meeting_dict['user'].pop('password')
	return jsonify(
		data=meetings_dicts,
		message="successfully showed all meetings",
		status=200
	),200

@meetings.route('/', methods=['POST'])
@login_required
def create_meeting():
	payload = request.get_json()
	new_meeting = models.Meeting.create(
		user=current_user.id,
		info=payload['info'],
		area=payload['area'],
		time=payload['time']

	)
	meeting_dict = model_to_dict(new_meeting)
	meeting_dict['user'].pop('password')
	return jsonify(
		data=meeting_dict,
		message="successfully posted",
		status=200
	),200

@meetings.route('/<id>', methods=['DELETE'])
@login_required
def delete_meeting(id):
	meeting_to_delete = models.Meeting.get_by_id(id)
	if current_user.id == meeting_to_delete.user.id:
		delete_query = models.Meeting.delete().where(models.Meeting.id == id)
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

@meetings.route('/<id>', methods=['PUT'])
@login_required
def update_meeting(id):
	payload = request.get_json()
	meeting_to_update = models.Meeting.get_by_id(id)
	if current_user.id == meeting_to_update.user.id:
		if 'info' in payload:
			meeting_to_update.info=payload['info']
		if 'area' in payload:
			meeting_to_update.area=payload['area']
		if 'time' in payload:
			meeting_to_update.time=payload['time']
		meeting_to_update.save()
		updated_meeting_dict = model_to_dict(meeting_to_update)
		updated_meeting_dict['user'].pop('password')
		return jsonify(
			data=updated_meeting_dict,
			message=f"succesfully updated {id}",
			status=200
		),200
	else:
		return jsonify(
			data={},
			message=f"you must be logged in to updated",
			status=403
		), 403





