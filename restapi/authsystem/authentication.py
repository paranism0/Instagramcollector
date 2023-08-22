from passlib.context import CryptContext
from ..models import credential

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class authenticationSystem:

   def __init__(self) -> None:
        ...

   def verify_password(self,  plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

   def get_password_hash(self, password):
        return pwd_context.hash(password)

   def get_user(self , db, username: str):
        if username in db:
          user_dict = db[username]
          return credential.UserInDB(**user_dict)

   def authenticate_user(self , fake_db, username: str, password: str):
        user = self.get_user(fake_db, username)
        if not user:
          return False
        if not self.verify_password(password, user.hashed_password):
          return False
        return user