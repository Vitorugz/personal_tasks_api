from functools import wraps
from flask import request, Response
from resources.jwt import validate

# This function is used to return "Access Denied" if username and password is not correct.
def unauthorized_response():
    return Response(
        "Access Denied",
        401
    )

# This is a decorator, used to check if username and password received is correct.
def requires_auth(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        authorization = request.headers.get('Authorization')
        if not authorization:
            return unauthorized_response()
        
        jwt_valid = validate(authorization)

        if "Error" in jwt_valid:
            return jwt_valid

        return function(*args, **kwargs)
    return decorator