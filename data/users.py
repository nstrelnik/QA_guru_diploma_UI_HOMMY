import dataclasses

# @dataclass
# class User:
#     login: str
#     password: str
#     name: Optional[str] = None
#     country: Optional[str] = None
#     city: Optional[str] = None
#     credit_card: Optional[str] = None
#     month: Optional[str] = None
#     year: Optional[str] = None

@dataclasses.dataclass
class User:
    user_email: str
    user_password: str

