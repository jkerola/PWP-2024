"""Contains the API Configuration"""

from dataclasses import dataclass
from os import getenv
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


@dataclass()
class Config:
    """Utility class containing API configuration options"""

    secret: str = getenv("SECRET_TOKEN")
    jwt_expires_in = timedelta(minutes=30)

    def __post_init__(self):
        if self.secret is None or len(self.secret) == 0:
            raise KeyError("Couldn't load secret from env")


config = Config()
