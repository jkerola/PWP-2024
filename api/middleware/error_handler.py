"""Contains a minimalistic error handler"""

from flask import make_response
from werkzeug.exceptions import HTTPException


def handle_exception(e: HTTPException):
    """Error handler middleware

    converts any werkzeug error into a JSON response
    """
    payload = {"error": e.name, "code": e.code, "description": e.description}
    return make_response(payload), e.code
