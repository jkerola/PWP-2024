from flask import Blueprint, make_response, Response
from api.middleware.authguard import requires_strong_authentication
from prisma.models import User

users_bp = Blueprint("users", __name__)


@users_bp.get("/users")
@requires_strong_authentication
def get_users(user: User):
    users = User.prisma().find_many()
    return make_response([user.model_dump(exclude=["hash"]) for user in users])


@users_bp.delete("/users/<userId>")
@requires_strong_authentication
def delete_user(userId: str, user: User):
    User.prisma().delete(where={"id": userId})
    return Response(status=204)
