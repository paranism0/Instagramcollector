from pydantic import BaseModel

class insta_user_before_login(BaseModel):
    username : str
    password : str