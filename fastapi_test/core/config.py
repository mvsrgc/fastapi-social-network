import os

from pydantic import BaseSettings


class settings(BaseSettings):
    API_V1_PREFIX = "/api/v1"
    SECRET_KEY = os.environ["SECRET_KEY"]
    DATABASE_URL = os.environ["DATABASE_URL"]
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = settings()
