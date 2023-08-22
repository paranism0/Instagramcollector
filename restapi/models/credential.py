from pydantic import BaseModel
from typing import Any

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None

class NewUser(BaseModel):
    full_name: str
    username: str
    email: str
    password: str

class UserInDB(User):
    _id : Any
    password : str