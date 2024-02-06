from dataclasses import dataclass, asdict
from argon2 import PasswordHasher


class _BaseDto:
    username: str
    password: str
    _ph = PasswordHasher()

    def __post_init__(self):
        if self.username is None:
            raise Exception("Missing property: 'username'")
        if self.password is None:
            raise Exception("Missing property: 'password'")

    def generate_hash(self) -> str:
        return self._ph.hash(self.password)


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
        return self._ph.verify(hash, self.password)

    @staticmethod
    def from_json(data: dict):
        return LoginDto(
            username=data.get("username"),
            password=data.get("password"),
        )
