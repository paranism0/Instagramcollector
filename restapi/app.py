from fastapi import FastAPI , Depends , Form
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from .models.credential import Token , User , NewUser
from .authsystem.authorization import authorizationSystem
import instagram

auth = authorizationSystem()
instaObj = instagram.handleInstagram()
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

@app.post("/users/create")
async def create_user(user : Annotated[NewUser , Depends(auth.create_new_user)]):
    return user

@app.post("/users/addAccount")
async def add_instagram_account(user : Annotated[User,Depends(get_current_active_user)] , form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    result = await instaObj.login(form_data.username , form_data.password)
    return result

@app.post("/users/getfollowers")
async def get_followers(user : Annotated[User,Depends(get_current_active_user)] , \
    username: Annotated[str, Form()], account_id: Annotated[str, Form()]):
    followers = await instaObj.get_followers(account_id , username)
    return followers