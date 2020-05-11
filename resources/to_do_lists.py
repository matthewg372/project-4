import models
from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict


to_do_lists = Blueprint('to_do_lists', 'to_do_lists')

@to_do_lists.route('/users/<id>', methods=['GET'])
@login_required
def user_products_index(id):
	user_to_do_list = models.User.get_by_id(id)
	current_user_to_do_list_dicts = [model_to_dict(to_do_list) for to_do_list in user_to_do_list.ToDoLists]
	print(current_user_to_do_list_dicts)
	for to_do_list_dict in current_user_to_do_list_dicts:
		to_do_list_dict['user'].pop('password')
	return jsonify(
		data= current_user_to_do_list_dicts,
		message= f"Successfully found {len(current_user_to_do_list_dicts)} list",
		status= 200
	), 200

@to_do_lists.route('/', methods=['POST'])
@login_required
def create_to_do_list():
	payload = request.get_json()
	new_list = models.To_Do_List.create(
		user=current_user.id,
		item=payload['item']
		)
	list_item_dict = model_to_dict(new_list)
	list_item_dict['user'].pop('password')
	return jsonify(
		data=list_item_dict,
		message=f"successfully created list item",
		status=200
	),200

@to_do_lists.route('/<id>', methods=['DELETE'])
@login_required
def delete_list_item(id):
	list_item_to_delete = models.To_Do_List.get_by_id(id)
	if current_user.id == list_item_to_delete.user.id:
		delete_query = models.To_Do_List.delete().where(models.To_Do_List.id == id)
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




