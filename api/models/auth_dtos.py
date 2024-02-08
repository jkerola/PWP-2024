from dataclasses import dataclass, asdict
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from werkzeug.exceptions import BadRequest


class _BaseDto:
    username: str
    password: str
    _ph = PasswordHasher()

    def generate_hash(self) -> str:
        return self._ph.hash(self.password)

    def _validate(data: dict) -> [str]:
        validators = ["username", "password"]
        errors = []
        for validator in validators:
            val = data.get(validator)
            if val is None:
                errors.append(f"Missing property '{validator}'")
            elif not isinstance(val, str):
                errors.append(f"Property '{validator}' not of type str")
        return errors


@dataclass(frozen=True)
class RegisterDto(_BaseDto):
    username: str
    password: str
    email: str = None
    firstName: str = None
    lastName: str = None

    def to_dict(self) -> dict:
        user = {k: str(v) for k, v in asdict(self).items()}
        user["hash"] = self.generate_hash()
        del user["password"]
        return user

    @staticmethod
    def from_json(data: dict):
        errors = LoginDto._validate(data)
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
        try:
            return self._ph.verify(hash, self.password)
        except VerifyMismatchError:
            raise BadRequest("Invalid credentials")

    @staticmethod
    def from_json(data: dict):
        errors = LoginDto._validate(data)
        if len(errors) > 0:
            raise BadRequest(errors)
        return LoginDto(
            username=data.get("username"),
            password=data.get("password"),
        )
