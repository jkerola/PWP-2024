"Contains decorator functions related to authenticated routes"

from functools import wraps
import requests
from flask import request
from werkzeug.exceptions import Unauthorized, Forbidden
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
    def parse_authorization(*args, **kwargs):
        auth_type = None
        token = None
        try:
            if "Authorization" in request.headers:
                auth_type, token = request.headers["Authorization"].split(" ")
            if not token or auth_type != "Bearer":
                raise Unauthorized("unauthorized request")
            data = JWTService.verify_token(token)
            user = db.user.find_unique({"id": data["sub"]})
            kwargs["user"] = user
            if not user:
                raise Unauthorized("unauthorized request")
        except (ValueError, DecodeError):
            raise Unauthorized("unauthorized request")
        return f(*args, **kwargs)

    return parse_authorization


def optional_authorization(f):
    """Decorator function which checks for authenticated users, but does not require it."""

    @wraps(f)
    def parse_optional_authorization(*args, **kwargs):
        auth_type = None
        token = None
        try:
            kwargs["user"] = None
            if "Authorization" in request.headers:
                auth_type, token = request.headers["Authorization"].split(" ")
            if not token or auth_type != "Bearer":
                return f(*args, **kwargs)
            data = JWTService.verify_token(token)
            user = db.user.find_unique({"id": data["sub"]})
            if user:
                kwargs["user"] = user
        except (ValueError, DecodeError, Unauthorized):
            kwargs["user"] = None
        return f(*args, **kwargs)

    return parse_optional_authorization


def requires_strong_authentication(f):
    """Decorator function which uses auxiliary services to authenticate a user."""

    @wraps(f)
    def get_strong_auth(*args, **kwargs):
        auth_type = None
        token = None
        try:
            if "Authorization" in request.headers:
                auth_type, token = request.headers["Authorization"].split(" ")
            if not token or auth_type != "Bearer":
                raise Unauthorized("unauthorized request")
            data = JWTService.verify_token(token)
            user = db.user.find_unique({"id": data["sub"]})
            response = requests.get("http://localhost:5001/auth", {"userId": user.id})
            if response.status_code != 200:
                raise Forbidden("forbidden request")
            if not user:
                raise Unauthorized("unauthorized request")
            kwargs["user"] = user
        except (ValueError, DecodeError):
            raise Unauthorized("unauthorized request")
        return f(*args, **kwargs)

    return get_strong_auth
