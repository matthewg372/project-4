import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required


posts = Blueprint('posts', 'posts')

# @posts.route('/<id>', methods=['GET'])
# def all_posts(id):
# 		user_posts = models.User.get_by_id(id)
# 		friends_posts = models.Friendship['user2'].get_by_id(id)
# 		current_user_post_dicts = [model_to_dict(post) for post in user_posts.posts]
# 		current_friend_post_dicts = [model_to_dict(post) for post in friends_posts.posts]
# 		for post_dict in current_user_post_dicts:
# 			post_dict['user'].pop('password')
# 		for friend_post_dict in current_friend_post_dicts:
# 			friend_post_dict['user'].pop('password')
# 		if models.DoesNotExist:
# 			return jsonify(
# 				data={current_user_post_dicts},
# 				message="successfully found posts",
# 				status=200
# 			),200
# 		else:
# 			return jsonify(
# 				data={current_friend_post_dicts, current_user_post_dicts},
# 				message="successfully found posts",
# 				status=200
# 			),200




@posts.route('/<id>', methods=['GET'])
@login_required
def all_posts(id):
		user_posts = models.User.get_by_id(id)
		current_user_post_dicts = [model_to_dict(post) for post in user_posts.posts]	
		for post_dict in current_user_post_dicts:
			post_dict['user'].pop('password')
		if models.DoesNotExist:
			return jsonify(
				data=current_user_post_dicts,
				message="successfully found posts",
				status=200
			),200



@posts.route('/all/<id>', methods=['GET'])
def all(id):
		user = models.User.get_by_id(id)
		posts = []
		for friendship in user.friends:
			posts_dicts = [model_to_dict(post) for post in friendship.user1.posts]
			for friends_posts in posts_dicts:
				friends_posts['user'].pop('password')
				posts.append(friends_posts)
				print(friends_posts)

		return jsonify(
			data=posts,
			message=f"successfully found {len(friends_posts)} posts ",
			status=200
		),200

@posts.route('/', methods=['POST'])
@login_required
def create_posts():
	payload = request.get_json()
	new_post = models.Post.create(
		user=current_user.id,
		bio=payload['bio'],
		images=payload['images']
	)
	post_dict = model_to_dict(new_post)
	post_dict['user'].pop('password')
	return jsonify(
		data=post_dict,
		message="successfully posted",
		status=200
	),200


""" delete specific post """
@posts.route('/<id>', methods=['DELETE'])
@login_required
def delete_post(id):
	post_to_delete = models.Post.get_by_id(id)
	if current_user.id == post_to_delete.user.id:
		delete_query = models.Post.delete().where(models.Post.id == id)
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

@posts.route('/<id>', methods=['PUT'])
@login_required
def update_post(id):
	payload = request.get_json()
	post_to_update = models.Post.get_by_id(id)
	if current_user.id == post_to_update.user.id:
		if 'bio' in payload:
			post_to_update.bio=payload['bio']
		post_to_update.save()
		updated_post_dict = model_to_dict(post_to_update)
		updated_post_dict['user'].pop('password')
		return jsonify(
			data=updated_post_dict,
			message=f"succesfully updated {id}",
			status=200
		),200
	else:
		return jsonify(
			data={},
			message=f"you must be logged in to updated",
			status=403
		), 403

