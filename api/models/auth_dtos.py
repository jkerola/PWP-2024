"""Contains DTOs related to authentication"""

from dataclasses import dataclass
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from werkzeug.exceptions import BadRequest
from api.models.base_dto import BaseDto


# In order to keep JSON -> Python conversion easily readable,
# we use the original camelCase naming convention
# pylint: disable=invalid-name


@dataclass(frozen=True)
class RegisterDto(BaseDto):
    """DTO for managing user signup"""

    username: str
    hash: str
    email: str = None
    firstName: str = None
    lastName: str = None

    @staticmethod
    def from_json(data: dict):
        """Creates a new Dto from request.json
        data: request.json
        """
        RegisterDto.validate(
            data,
            {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                    "email": {"type": "string"},
                    "firstName": {"type": "string"},
                    "lastName": {"type": "string"},
                },
                "required": ["username", "password"],
            },
        )
        return RegisterDto(
            username=data.get("username"),
            hash=PasswordHasher().hash(data.get("password")),
            email=data.get("email"),
            firstName=data.get("firstName"),
            lastName=data.get("lastName"),
        )


@dataclass(frozen=True)
class LoginDto(BaseDto):
    """DTO for managing user authentication"""

    username: str
    password: str

    def verify(self, password_hash: str) -> bool:
        """Compares the login password to [password_hash]
        hash: str
        returns True if match, else raise BadRequest
        """
        try:
            return PasswordHasher().verify(password_hash, self.password)
        except VerifyMismatchError:
            raise BadRequest("Invalid credentials")

    @staticmethod
    def from_json(data: dict):
        """Creates a new DTO from json
        data: request.json
        """
        LoginDto.validate(
            data,
            {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                },
                "required": ["username", "password"],
            },
        )

        return LoginDto(
            username=data.get("username"),
            password=data.get("password"),
        )
