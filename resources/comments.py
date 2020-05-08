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

	return jsonify(
		data=comment_dict,
		message="successfull commented",
		status=200
	),200

@comments.route('/<id>', methods=['DELETE'])
def delete_comments(id):
	comment_to_delete = models.Comment.get_by_id(id)
	if current_user.id == comment_to_delete.user.id:
		delete_query = models.Comment.delete().where(models.Comment.id == id)
		delete_query.execute()
		return jsonify(
			data={},
			message=f"succesfully deleted {id}",
			status=200
		), 200
	else:
		return jsonify(
			data={},
			message="you must be logged in to delete this",
			status=403
		), 403

@comments.route('/<id>', methods=['PUT'])
def update_product(id):
	payload = request.get_json()
	comment_to_update = models.Comment.get_by_id(id)
	if current_user.id == comment_to_update.user.id:
		if 'bio' in payload:
			comment_to_update.bio=payload['bio']
		comment_to_update.save()
		updated_comment_dict = model_to_dict(comment_to_update)
		updated_comment_dict['user'].pop('password')
		return jsonify(
			data=updated_comment_dict,
			message=f"succesfully updated {id}",
			status=200
		),200
	else:
		return jsonify(
			data={},
			message=f"you must be logged in to updated",
			status=403
		), 403




