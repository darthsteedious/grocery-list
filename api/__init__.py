from program import app, execute

GET, PUT, POST, DELETE, PATCH, OPTIONS, HEAD = tuple(
    [x.upper() for x in ['GET', 'PUT', 'POST', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD']]
)

import api.list
