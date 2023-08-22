from passlib.context import CryptContext
from ..models import credential
from ..models.status import msgstatus
from fastapi import HTTPException , status
from pymongo.errors import DuplicateKeyError
from ..enums.authenum import resultmsg as requestresult , resulttype as request_result_type
from ..database.handleUsers import Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class authenticationSystem(Users):

   def __init__(self) -> None:
        super().__init__()

   def verify_password(self,  plain_password, hashed_password):
         return pwd_context.verify(plain_password, hashed_password)

   def get_password_hash(self, password):
        return pwd_context.hash(password)
   
   async def create_new_user(self , user : credential.NewUser):
        try:
          user.password = self.get_password_hash(user.password)
          result = await self.insert(user.model_dump(),self.users)
          if result.inserted_id!=None:
            request_status = request_result_type.OK
            request_msg = requestresult.SUCCESS
        except DuplicateKeyError as dup:
          request_status = request_result_type.FAIL
          request_msg = requestresult.DUPLICATE
        except Exception as e:
          request_status = request_result_type.FAIL
          request_msg = requestresult.ERROR
        return msgstatus(status=request_status , msg=request_msg)

   async def get_user(self , username: str):
        result = await self.select({"username" : username},self.users)
        if isinstance(result , dict) and len(result)>0:
          return credential.UserInDB(**result)
        return False
   
   def raise_auth_error(self):
      raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Incorrect username or password",
              headers={"WWW-Authenticate": "Bearer"},
            )

   async def authenticate_user(self , username: str, password: str):
        user = await self.get_user(username)
        if not user:
            self.raise_auth_error()
        if not self.verify_password(password, user.password):
            self.raise_auth_error()
        else:
            return user