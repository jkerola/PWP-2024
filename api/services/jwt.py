"""Contains the JWTService class"""

from datetime import datetime, timezone
from werkzeug.exceptions import Unauthorized
import jwt
from api.config import config


class JWTService:
    """Service class for managing JWTs"""

    @staticmethod
    def create_token(payload: dict) -> str:
        """Creates a JWT token with the given payload"""
        expires_in = datetime.now(tz=timezone.utc) + config.jwt_expires_in

        return jwt.encode({"exp": expires_in, **payload}, config.secret)

    @staticmethod
    def verify_token(token: str) -> dict:
        """Verifies and decodes the given token
        raises Unauthorized on failure
        """
        try:
            return jwt.decode(token, config.secret, ["HS256"])
        except jwt.exceptions.ExpiredSignatureError:
            raise Unauthorized("token expired")
