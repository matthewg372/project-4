import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required


comments = Blueprint('comments', 'comments')


@comments.route('/<id>', methods=['POST'])
def create_comment(id):
	payload = request.get_json()
	post_id = models.Post.get_by_id(id)
	new_comments = models.Comment.create(
		user=current_user.id,
		bio=payload['bio'],
		post=post_id
	)
	comment_dict = model_to_dict(new_comments)
	comment_dict['user'].pop('password')
	comment_dict['user'].pop('password')

	return jsonify(
		data=comment_dict,
		message="successfull commented",
		status=200
	),200