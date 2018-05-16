from flask import request, jsonify
from api import app, execute, GET, POST


def insert_list(conn, cur):
    cur.execute('''
    INSERT INTO grocery.grocery_list(completed)
    SELECT NULL 
    WHERE NOT EXISTS (SELECT 1 FROM grocery.grocery_list gl WHERE gl.completed IS NULL)
    ON CONFLICT DO NOTHING
    RETURNING id
    ''')
    result = cur.fetchone()
    conn.commit()

    return result


def get_list(_, cur):
    cur.execute('SELECT id, completed FROM grocery.grocery_list WHERE completed IS NULL LIMIT 1')
    return cur.fetchone()


def set_list_complete(conn, cur, list_id):
    cur.execute('''
    UPDATE grocery.grocery_list
    SET completed = now(), modified_at = now()
    WHERE id = %s
    ''', (list_id,))

    conn.commit()


def get_list_items(_, cur, list_id):
    cur.execute('''
    SELECT id, name, description
    FROM grocery.grocery_list_item gli
    WHERE gli.grocery_list_id = %s
    ''', (list_id,))
    return cur.fetchall()


def list_index_get():
    result = execute(get_list)
    if result is None:
        return jsonify(None), 200

    list_id, completed = result

    items_result = [{'id': list_id, 'name': name, 'description': description} for (list_id, name, description) in
                    execute(get_list_items, list_id)]
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
