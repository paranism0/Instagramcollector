from typing import Annotated
from fastapi import Depends, HTTPException, status
from .jwt import Jwt
from fastapi.security import OAuth2PasswordBearer
from .authentication import authenticationSystem

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class authorizationSystem(authenticationSystem):
    
    def __init__(self):
        self.jwtObj = Jwt()
        self.fake_users_db = {
        "johndoe": {
          "username": "johndoe",
          "full_name": "John Doe",
          "email": "johndoe@example.com",
          "hashed_password": "$2b$12$SXeBux6a7vrvvWCpPJCBaeqYEsccqqzNaDMHa87xalcI7WBarjtHu",
          "disabled": False,
          }
        }

    async def get_current_user(self , token: Annotated[str, Depends(oauth2_scheme)]):
      credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
      )
      token_data = self.jwtObj.get_token_data(token)
      user = self.get_user(self.fake_users_db, username=token_data.username)
      if user is None:
         raise credentials_exception
      return user