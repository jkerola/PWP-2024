"""Contains DTOs related to authentication"""

from dataclasses import dataclass, asdict
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from werkzeug.exceptions import BadRequest
from api.models.base_dto import BaseDto


# In order to keep JSON -> Python conversion easily readable,
# we use the original camelCase naming convention
# pylint: disable=invalid-name


class _AuthBaseDto(BaseDto):
    _ph = PasswordHasher()


@dataclass(frozen=True)
class RegisterDto(_AuthBaseDto):
    """DTO for managing user signup"""

    username: str
    password: str
    email: str = None
    firstName: str = None
    lastName: str = None

    def generate_hash(self) -> str:
        """Creates a salted hash of the password property."""
        return self._ph.hash(self.password)

    def to_insertable(self) -> dict:
        """Converts the password into a salted hash and
        returns the DTO as a dict."""
        user = {k: str(v) for k, v in asdict(self).items()}
        user["hash"] = self.generate_hash()
        del user["password"]
        return user

    @staticmethod
    def from_json(data: dict):
        """Creates a new Dto from request.json
        data: request.json
        """
        RegisterDto.validate(
            [
                ("username", str),
                ("password", str),
            ],
            data,
        )
        return RegisterDto(
            username=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
            firstName=data.get("firstName"),
            lastName=data.get("lastName"),
        )


@dataclass(frozen=True)
class LoginDto(_AuthBaseDto):
    """DTO for managing user authentication"""

    username: str
    password: str

    def verify(self, password_hash: str) -> bool:
        """Compares the login password to [password_hash]
        hash: str
        returns True if match, else raise BadRequest
        """
        try:
            return self._ph.verify(password_hash, self.password)
        except VerifyMismatchError:
            raise BadRequest("Invalid credentials")

    @staticmethod
    def from_json(data: dict):
        """Creates a new DTO from json
        data: request.json
        """
        LoginDto.validate(
            [
                ("username", str),
                ("password", str),
            ],
            data,
        )

        return LoginDto(
            username=data.get("username"),
            password=data.get("password"),
        )
