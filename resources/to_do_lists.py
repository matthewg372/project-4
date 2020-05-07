import models
from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict


to_do_lists = Blueprint('to_do_lists', 'to_do_lists')

@to_do_lists.route('/', methods=['POST'])
def create_to_do_list():
	payload = request.get_json()
	new_list = models.To_Do_List.create(
		user=current_user.id,
		To_Do_Item=payload['to_do_item']
		)
	list_item_dict = model_to_dict(new_list)
	list_item_dict['user'].pop('password')
	return jsonify(
		data=list_item_dict,
		message=f"successfully created list item",
		status=200
	),200