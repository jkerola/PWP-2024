from dotenv import load_dotenv
from dataclasses import dataclass
from os import getenv

load_dotenv()


@dataclass()
class Config:
    secret: str = getenv("SECRET_TOKEN")

    def __post_init__(self):
        if self.secret is None or len(self.secret) == 0:
            raise Exception("Couldn't load secret from env")


config = Config()
