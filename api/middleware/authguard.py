"Contains decorator functions related to authenticated routes"
from functools import wraps
from flask import request
from werkzeug.exceptions import Unauthorized
from jwt.exceptions import DecodeError
from api.services.jwt import JWTService
from api.database import db


def requires_authentication(f):
    """Decorator function which protects routes from unauthorized access

    usage:
    @requires_authentication()
    @route.get("/")
    def my_route(user):
        <do stuff with the authenticated user information>
    """

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
