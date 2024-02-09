from dataclasses import dataclass, asdict
from typing import List
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from werkzeug.exceptions import BadRequest


class _BaseDto:
    username: str
    password: str
    _ph = PasswordHasher()

    def generate_hash(self) -> str:
        """Creates a salted hash of the password property."""
        return self._ph.hash(self.password)

    def _validate(data: dict) -> List[str]:
        props = ["username", "password"]
        errors = []
        for prop in props:
            val = data.get(prop)
            if val is None:
                errors.append(f"Missing property '{prop}'")
            elif not isinstance(val, str):
                errors.append(f"Property '{prop}' not of type str")
        return errors


@dataclass(frozen=True)
class RegisterDto(_BaseDto):
    username: str
    password: str
    email: str = None
    firstName: str = None
    lastName: str = None

    def to_insertable(self) -> dict:
        """Converts the password into a salted hash and
        returns the DTO as a dict."""
        user = {k: str(v) for k, v in asdict(self).items()}
        user["hash"] = self.generate_hash()
        del user["password"]
        return user

    @staticmethod
    def from_json(data: dict):
        """Creates a new Dto from request.json"""
        errors = RegisterDto._validate(data)
        if len(errors) > 0:
            raise BadRequest(errors)
        return RegisterDto(
            username=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
            firstName=data.get("firstName"),
            lastName=data.get("lastName"),
        )


@dataclass(frozen=True)
class LoginDto(_BaseDto):
    username: str
    password: str

    def verify(self, hash: str) -> bool:
        """Compares the login password to [hash]
        returns True if match, else raise BadRequest"""
        try:
            return self._ph.verify(hash, self.password)
        except VerifyMismatchError:
            raise BadRequest("Invalid credentials")

    @staticmethod
    def from_json(data: dict):
        """Creates a new Dto from request.json"""
        errors = LoginDto._validate(data)
        if len(errors) > 0:
            raise BadRequest(errors)
        return LoginDto(
            username=data.get("username"),
            password=data.get("password"),
        )
