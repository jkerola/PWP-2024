from flask import request, make_response, Blueprint, Response
from api.models.auth_dtos import RegisterDto, LoginDto
from prisma.errors import UniqueViolationError
from api.services.jwt import JWTService
from api.middleware.authguard import requires_authentication
from prisma.models import User
from werkzeug.exceptions import Unauthorized, BadRequest

auth = Blueprint("auth", __name__)


@auth.route("/auth/register", methods=["POST"])
def register():
    register_dto = RegisterDto.from_json(request.json)
    try:
        User.prisma().create(data=register_dto.to_insertable())
    except UniqueViolationError:
        raise BadRequest("username not unique")
    return Response(status=201)


@auth.route("/auth/login", methods=["POST"])
def login():
    login_dto = LoginDto.from_json(request.json)
    user = User.prisma().find_first(where={"username": login_dto.username})
    if user and login_dto.verify(user.hash):
        payload = {"sub": user.id, "username": user.username}
        token = JWTService.create_token(payload)
        return make_response({"access_token": token})
    else:
        raise Unauthorized("unauthorized request")


@auth.route("/auth/profile", methods=["GET"])
@requires_authentication
def profile(user: User):
    user_dict = user.model_dump()
    del user_dict["hash"]
    return user_dict
