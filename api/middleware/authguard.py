from functools import wraps
from flask import request
from api.services.jwt import JWTService
from api.database import db
from werkzeug.exceptions import Unauthorized
from jwt.exceptions import DecodeError


def requires_authentication(f):
    @wraps(f)
    def parse_authorization():
        auth_type = None
        token = None
        try:
            if "Authorization" in request.headers:
                auth_type, token = request.headers["Authorization"].split(" ")
            if not token or auth_type != "Bearer":
                raise Unauthorized("unauthorized request")
            data = JWTService.verify_token(token)
            user = db.user.find_unique({"id": data["sub"]})
            if not user:
                raise Unauthorized("unauthorized request")
        except (ValueError, DecodeError):
            raise Unauthorized("unauthorized request")
        return f(user)

    return parse_authorization
