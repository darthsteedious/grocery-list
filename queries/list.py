from program import execute


def insert_list():
    def query(conn, cur):
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

    return execute(query)


def get_list():
    def query_list(_, cur):
        cur.execute('SELECT id, completed FROM grocery.grocery_list WHERE completed IS NULL LIMIT 1')
        return cur.fetchone()

    return execute(query_list)


def get_list_items(list_id):
    def query(_, cur, list_id):
        cur.execute('''
        SELECT id, name, description
        FROM grocery.grocery_list_item gli
        WHERE gli.grocery_list_id = %s
        ''', (list_id,))
        return cur.fetchall()

    return execute(query, list_id)


def set_list_complete(list_id):
    def query(conn, cur, list_id):
        cur.execute('''
        UPDATE grocery.grocery_list
        SET completed = now(), modified_at = now()
        WHERE id = %s
        ''', (list_id,))
        conn.commit()

    return execute(query, list_id)
