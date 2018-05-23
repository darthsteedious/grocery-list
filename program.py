from db import create_execute_async
from aiohttp import web
import ssl
from pathlib import Path

routes = web.RouteTableDef()

conn_str = 'dbname=grocerydb'

execute = create_execute_async(conn_str)

import api.list

p = Path('.').resolve()
cert_file = p.joinpath('cert.pem').resolve()
# key_file = p.joinpath('server.key').resolve()
#
ssl_context = ssl.SSLContext()
ssl_context.load_cert_chain(cert_file)

app = web.Application()
app.add_routes(routes)
web.run_app(app, ssl_context=ssl_context)


# import api

#
# if __name__ == '__main__':
#     app.run()
