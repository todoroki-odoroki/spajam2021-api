from typing import List
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

# DATABASE_URL = config("DB_CONNECTION", cast=)

MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret ,default="secret")

API_PREFIX: str = config("API_PREFIX", default="api")

PROJECT_NAME: str = config("PROJECT_NAME", default="Spajam API")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="*",
)