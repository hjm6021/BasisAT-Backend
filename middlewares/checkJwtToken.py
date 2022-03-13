from functools import wraps
from flask import request, abort


def checkJwtTokenMiddleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        jwtAccessToken = request.cookies.get("access-token")

        if jwtAccessToken is None:
            abort(401)

        return func(*args, **kwargs)

    return decorated_function
