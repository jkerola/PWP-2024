from functools import wraps
from flask import request
from services.jwt import JWTService
from database import db
from models.errors import ApiException


def requires_authentication(f):
    @wraps(f)
    def parse_authorization():
        try:
            auth_type = None
            token = None
            if "Authorization" in request.headers:
                auth_type, token = request.headers["Authorization"].split(" ")
            if not token or auth_type != "Bearer":
                raise ApiException("Unauthorized")
            data = JWTService.verify_token(token)
            user = db.user.find_unique({"id": data["sub"]})
            if not user:
                raise ApiException("Unauthorized")
        except ApiException as e:
            return e.to_json(), 401
        return f(user)

    return parse_authorization
