from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    APP_ENV: str = 'local'
    PROJECT_NAME: str = 'fastapi-sample'
    API_V1_STR: str = '/v1'
    SKIP_ROUTES: list = ['/redoc','/docs','/openapi.json']
    SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
    SQLALCHEMY_CONNECT_ARGS = {"check_same_thread": False}

# os.environ["APP_ENV"] = 'dev'

settings = Settings(_env_file=f'conf/{os.getenv("APP_ENV")}.env')
