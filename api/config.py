import os

from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")


VERSION: str = "0.0.1"
DEBUG: bool = config("DEBUG", cast=bool, default=True)
APP_NAME: str = "Whisper-API"
SECRET_KEY: str = config("SECRET_KEY", cast=Secret)
