from program import execute


async def insert_list():
    async def query(cur):
        await cur.execute('''
            INSERT INTO grocery.grocery_list(completed)
            SELECT NULL 
            WHERE NOT EXISTS (SELECT 1 FROM grocery.grocery_list gl WHERE gl.completed IS NULL)
            ON CONFLICT DO NOTHING
            RETURNING id
            ''')
        result = await cur.fetchone()
        return result

    return await execute(query)


async def get_list():
    async def query_list(cur):
        await cur.execute('SELECT id, completed FROM grocery.grocery_list WHERE completed IS NULL LIMIT 1')
        return await cur.fetchone()

    return await execute(query_list)


async def get_list_items(list_id):
    async def query(cur):
        await cur.execute('''
        SELECT id, name, description
        FROM grocery.grocery_list_item gli
        WHERE gli.grocery_list_id = %s
        ''', (list_id,))
        return await cur.fetchall()

    return await execute(query)


async def set_list_complete(list_id):
    async def query(cur):
        await cur.execute('''
        UPDATE grocery.grocery_list
        SET completed = now(), modified_at = now()
        WHERE id = %s
        ''', (list_id,))

    return await execute(query)


async def put_list_item(list_id, item):
    async def query(cur):
        await cur.execute('''
        INSERT INTO grocery.grocery_list_item(name, description, grocery_list_id)
        SELECT %s, %s, %s
        WHERE NOT EXISTS (SELECT 1 from grocery.grocery_list_item gli WHERE gli.name = %s AND gli.grocery_list_id = %s)
        RETURNING id
        ''', (item['name'], item['description'], list_id, item['name'], list_id))

        return await cur.fetchone()

    return await execute(query)
