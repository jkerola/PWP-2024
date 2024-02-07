import jwt
from api.config import config
from datetime import datetime, timedelta


class JWTService:
    @staticmethod
    def create_token(payload: dict) -> str:
        expires_in = datetime.now() + timedelta(minutes=30)

        return jwt.encode({"exp": expires_in, **payload}, config.secret)

    @staticmethod
    def verify_token(token: str) -> dict:
        return jwt.decode(token, config.secret, ["HS256"])
