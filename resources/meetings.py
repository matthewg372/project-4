import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

meetings = Blueprint('meetings', 'meetings')



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