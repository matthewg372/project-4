import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

friendships = Blueprint('friendships', 'friendships')


@friendships.route('/user/<id>', methods=['GET'])
@login_required
def find_friends(id):
	user_frindship = models.User.get_by_id(id)
	current_user_friendship_dicts = [model_to_dict(friendship) for friendship in user_frindship.friends]
	for friendship_dict in current_user_friendship_dicts:
		friendship_dict['user2'].pop('password')
		friendship_dict['user1'].pop('password')
	print(current_user_friendship_dicts)
	return jsonify(
		data=current_user_friendship_dicts,
		message=f"successfully found {len(current_user_friendship_dicts)} friends",
		status=200
	),200

@friendships.route('/<id>', methods=['POST'])
@login_required
def create_friendship(id):
		user = models.User.get_by_id(id)
		friends = [model_to_dict(friendship) for friendship in current_user.friends]
		try:
			if user == current_user :
				return jsonify(
					data={},
					message="can not be friends",
					status=401
				),401
			else:
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
		except: 
			return jsonify(
					data={},
					message="Except",
					status=401
				),401

@friendships.route('/<id>', methods=['DELETE'])
def delete_friend(id):
	friend_to_delete = models.Friendship.get_by_id(id)
	delete_query = models.Friendship.delete().where(models.Friendship.id == id)
	delete_query.execute()
	return jsonify(
		data={},
		message=f"succesfully deleted {id}",
		status=200
	), 200
