from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    MONGODB_HOST : str
    MONGODB_PORT : int = Field(ge=1 , le = 65535)
    model_config = SettingsConfigDict(env_file=".env")