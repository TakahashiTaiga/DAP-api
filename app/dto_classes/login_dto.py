from dataclasses import dataclass


@dataclass
class LoginDto():
    user_name: str
    user_id: int
