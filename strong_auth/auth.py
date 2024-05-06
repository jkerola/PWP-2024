from flask import Blueprint, request, make_response, Response

auth_controller = Blueprint("StrongAuth", __name__)


users = set()


def get_user_id(data: dict) -> str:
    if data["userId"] is None or not isinstance(data["userId"], str):
        return Response(status=400)
    return data["userId"]


@auth_controller.route("/auth/<user_id>", methods=["GET"])
def authenticate(user_id: str):
    if user_id in users:
        return Response(status=200)
    else:
        return Response(status=404)


@auth_controller.get("/users")
def get_users():
    return make_response(list(users))


@auth_controller.post("/users")
def add_user():
    user_id = get_user_id(request.json)
    users.add(user_id)
    return Response(status=201)
