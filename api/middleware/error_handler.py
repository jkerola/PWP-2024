from flask import make_response
from werkzeug.exceptions import HTTPException


def handle_exception(e: HTTPException):
    payload = {"error": e.name, "code": e.code, "description": e.description}
    return make_response(payload), e.code
