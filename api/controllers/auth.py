from flask import request, make_response, Blueprint, Response
from database import db
from models.auth_dtos import RegisterDto, LoginDto
from prisma.errors import UniqueViolationError
from models.errors import ApiException
from services.jwt import JWTService
from middleware.authguard import requires_authentication
from prisma.models import User

auth = Blueprint("auth", __name__)


@auth.route("/auth/register", methods=["POST"])
def register():
    try:
        register_dto = RegisterDto.from_json(request.json)
        db.user.create(data=register_dto.toUser())
        return Response(status=201)
    except UniqueViolationError:
        return make_response({"error": "username not unique"}, 400)
    except Exception as e:
        if type(e) == ApiException:
            e = e.to_json()
        return make_response(e, 400)


@auth.route("/auth/login", methods=["POST"])
def login():
    try:
        login_dto = LoginDto.from_json(request.json)
        user = db.user.find_first(where={"username": login_dto.username})
        if user and login_dto.verify(user.hash):
            payload = {"sub": user.id, "username": user.username}
            token = JWTService.create_token(payload)
            return make_response({"access_token": token})
        else:
            raise ApiException("Invalid credentials")
    except Exception as e:
        if type(e) == ApiException:
            e = e.to_json()
        return make_response(e, 400)


@auth.route("/auth/profile", methods=["GET"])
@requires_authentication
def profile(user: User):
    user_dict = user.model_dump()
    del user_dict["hash"]
    return user_dict
