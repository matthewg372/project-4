import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

friendships = Blueprint('friendships', 'friendships')


@friendships.route('/user/<id>', methods=['GET'])
def find_friends(id):
	user_frindship = models.User.get_by_id(id)
	current_user_friendship_dicts = [model_to_dict(friendship) for friendship in user_frindship.friends]
	for friendship_dict in current_user_friendship_dicts:
		friendship_dict['user2'].pop('password')
		friendship_dict['user1'].pop('password')
	return jsonify(
		data=current_user_friendship_dicts,
		message=f"successfully found {len(current_user_friendship_dicts)} friends",
		status=200
	),200

@friendships.route('/<id>', methods=['POST'])
def create_friendship(id):
	friend_id = models.User.get_by_id(id)
	new_friendship = models.Friendship.create(
		user1=friend_id,
		user2=current_user.id,
		)
	friendship_dict = model_to_dict(new_friendship)
	friendship_dict['user1'].pop('password')
	friendship_dict['user2'].pop('password')
	return jsonify(
		data=friendship_dict,
		message="made a friend",
		status=200
		),200

@friendships.route('/<id>', methods=['DELETE'])
def delete_friend(id):
	friend_to_delete = models.Friendship.get_by_id(id)
	if current_user.id == friend_to_delete.user1.id:
		delete_query = models.Friendship.delete().where(models.Friendship.id == id)
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