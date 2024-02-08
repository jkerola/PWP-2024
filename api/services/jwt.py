import jwt
from api.config import config
from datetime import datetime, timezone
from werkzeug.exceptions import Unauthorized


class JWTService:
    @staticmethod
    def create_token(payload: dict) -> str:
        expires_in = datetime.now(tz=timezone.utc) + config.jwt_expires_in

        return jwt.encode({"exp": expires_in, **payload}, config.secret)

    @staticmethod
    def verify_token(token: str) -> dict:
        try:
            return jwt.decode(token, config.secret, ["HS256"])
        except jwt.exceptions.ExpiredSignatureError:
            raise Unauthorized("token expired")
