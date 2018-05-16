import psycopg2
from flask import jsonify
from functools import wraps


def pg_error(error_messages):
    def decorator(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except psycopg2.Error as e:
                msg = error_messages.get(e.pgcode, None)
                if msg is not None:
                    return jsonify({'error': msg}), 500
        return decorator
    return decorator
