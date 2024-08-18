import dataclasses


@dataclasses.dataclass
class User:
    user_email: str
    user_password: str
