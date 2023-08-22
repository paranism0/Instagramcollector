from datetime import datetime, timedelta
from jose import jwt , JWTError
from ..models import env , credential
from fastapi import HTTPException , status

class Jwt:
  def __init__(self):
    vars = env.Settings()
    self.SECRET_KEY = vars.SECRET_KEY
    self.ALGORITHM = vars.ALGORITHM
    self.credentials_exception = HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail="Could not validate credentials",
         headers={"WWW-Authenticate": "Bearer"},
        )
  def create_jwt_token(self, data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
    return encoded_jwt

  def get_token_data(self,token):
    try:
        payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise self.credentials_exception
        token_data = credential.TokenData(username=username)
        return token_data
    except JWTError:
        raise self.credentials_exception