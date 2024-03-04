"""Module containing authentication routes"""

from flask import request, make_response, Blueprint, Response
from werkzeug.exceptions import Unauthorized, BadRequest
from prisma.models import User
from prisma.errors import UniqueViolationError
from api.middleware.authguard import requires_authentication
from api.models.auth_dtos import RegisterDto, LoginDto
from api.services.jwt import JWTService

auth = Blueprint("auth", __name__)


@auth.route("/auth/register", methods=["POST"])
def register():
    """Route for registering new users"""
    register_dto = RegisterDto.from_json(request.json)
    try:
        User.prisma().create(data=register_dto.to_insertable())
    except UniqueViolationError:
        raise BadRequest("username not unique")
    return Response(status=201)


@auth.route("/auth/login", methods=["POST"])
def login():
    """Route for authenticating users"""
    login_dto = LoginDto.from_json(request.json)
    user = User.prisma().find_first(where={"username": login_dto.username})
    if user and login_dto.verify(user.hash):
        payload = {"sub": user.id, "username": user.username}
        token = JWTService.create_token(payload)
        return make_response({"access_token": token})
    raise Unauthorized("unauthorized request")


@auth.route("/auth/profile", methods=["GET"])
@requires_authentication
def profile(user: User):
    """Route for fetching user information based on JWT contents"""
    user_dict = user.model_dump()
    del user_dict["hash"]
    return user_dict
