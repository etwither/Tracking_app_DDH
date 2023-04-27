# Authentication decorator
from functools import wraps
from flask import request, make_response, jsonify
import os


def require_bearer_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_token = None
        if 'Authorization' in request.headers:
            auth_token = request.headers['Authorization']
        if not auth_token or auth_token != 'Bearer ' + os.getenv('API_KEY'):
            return make_response(jsonify({"message": "missing api token"}), 401)
        return f(*args, **kwargs)
    return decorator