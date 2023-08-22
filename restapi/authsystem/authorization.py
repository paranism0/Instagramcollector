from typing import Annotated
from fastapi import Depends, HTTPException, status
from .jwt import Jwt
from fastapi.security import OAuth2PasswordBearer
from .authentication import authenticationSystem
from datetime import timedelta
from ..models import env

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class authorizationSystem(authenticationSystem):
    
    def __init__(self):
        super().__init__()
        self.vars = env.Settings()
        self.jwtObj = Jwt(self.vars)

    async def get_current_user(self , token: Annotated[str, Depends(oauth2_scheme)]):
      credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
      )
      token_data = self.jwtObj.get_token_data(token)
      user = await self.get_user(username=token_data.username)
      if user is None:
         raise credentials_exception
      return user
    
    def get_jwt_token(self , user):
        access_token_expires = timedelta(minutes=self.vars.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.jwtObj.create_jwt_token(
          data={"sub": user.username}, expires_delta=access_token_expires
        )
        return access_token