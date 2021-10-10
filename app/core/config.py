import logging
from typing import List

from loguru import logger
import sys
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from app.core.logging import InterceptHandler

config = Config(".env")

# ******application settigs******
DEBUG: bool = config("DEBUG", cast=bool, default=False)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="secret")
API_PREFIX: str = config("API_PREFIX", default="api")
PROJECT_NAME: str = config("PROJECT_NAME", default="Spajam API")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="*",
)


# *****database settings*****
DATABASE_URL: str = config("DB_CONNECTION", default="")
DB_USER: str = config("DB_USER", default="todoroki")
DB_NAME: str = config("DB_NAME", default="todoroki-db")
DB_PASS: str = config("DB_PASS", default="password")
DB_HOST: str = config("DB_HOST", default="localhost")
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)


# *****Externals*****
# ------AWS---------
AWS_ACCESS_KEY_ID: str = config("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY: str = config("AWS_SECRET_ACCESS_KEY", default="")
AWS_REGION: str = config("AWS_REGION", default="us-east-1")
AWS_BUCKET_NAME: str = config("AWS_BUCKET_NAME", default="spajam2021")
AWS_REKOGNITION_MODEL: str = config("AWS_REKOGNITION_MODEL", default="")


# *****Logging*****
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")
logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
