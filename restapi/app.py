from fastapi import FastAPI , HTTPException , Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from .models.credential import Token , User , NewUser
from .authsystem.authorization import authorizationSystem

auth = authorizationSystem()
app = FastAPI()

async def get_current_active_user(
    current_user: Annotated[User, Depends(auth.get_current_user)]
):
      return current_user

@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await auth.authenticate_user( form_data.username, form_data.password )
    access_token = auth.get_jwt_token(user)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/myinfo", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

@app.post("/users/add")
async def create_user(user : Annotated[NewUser , Depends(auth.create_new_user)]):
    return user