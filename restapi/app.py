from fastapi import FastAPI , status , HTTPException , Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta
from .models.credential import Token , User
from .models import env
from .authsystem.authorization import authorizationSystem
from .authsystem.jwt import Jwt

jwtObj = Jwt()
auth = authorizationSystem()
settings = env.Settings()
app = FastAPI()

async def get_current_active_user(current_user: Annotated[User, Depends(auth.get_current_user)]):
      if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
      return current_user

@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = auth.authenticate_user(auth.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwtObj.create_jwt_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/myinfo/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user