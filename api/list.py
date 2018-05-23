from queries.list import *
from program import routes, web


@routes.get('/api/list/')
async def index_get(request):
    result = await get_list()
    if result is None:
        return web.json_response(None, status=200)

    list_id, completed = result

    items_result = [{'id': list_id, 'name': name, 'description': description} for (list_id, name, description) in
                    await get_list_items(list_id)]
    return web.json_response({'id': list_id, 'completed': completed, 'items': items_result}, status=200)


@routes.post('/api/list/')
async def index_post(request):
    result = await insert_list()
    if result is None:
        return web.Response(status=204)

    # list_id, = result
    return web.json_response('', status=201, headers={'Location': '/api/list'})


@routes.put('/api/list/{list_id:\d+}')
async def complete_list(request):
    await set_list_complete(request.match_info['list_id'])
    await insert_list()
    return web.Response(status=204)


@routes.post('/api/list/{list_id:\d+}/item')
async def put_item(request):
    result = await request.json()
    list_id = request.match_info['list_id']
    result = await put_list_item(list_id, result)
    if result is None:
        return web.Response(text='Item exists', status=400)

    (item_id,) = result
    return web.Response(status=201, headers={'Location': f'/api/list/{list_id}/item/{item_id}'})
