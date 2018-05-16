from flask import request, jsonify
from api import app, execute, GET, POST
from queries.list import *


def list_index_get():
    result = get_list()
    if result is None:
        return jsonify(None), 200

    list_id, completed = result

    items_result = [{'id': list_id, 'name': name, 'description': description} for (list_id, name, description) in
                    get_list_items(list_id)]
    return jsonify({'id': list_id, 'completed': completed, 'items': items_result}), 200


def list_index_post():
    result = execute(insert_list)
    if result is None:
        return '', 204

    list_id, = result
    print(list_id)
    return jsonify(), 201, {'Location': '/api/list'}


@app.route('/api/list', methods=[GET, POST])
def index():
    if request.method == 'GET':
        return list_index_get()
    else:
        return list_index_post()


@app.route('/api/list/<int:list_id>/complete', methods=['PUT'])
def update_list(list_id):
    execute(set_list_complete, list_id)
    return jsonify(''), 204
