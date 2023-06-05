import os
from pydantic import BaseConfig
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class ReadEnv(BaseConfig):
    FAKER_LANGUAGE = os.getenv('FAKER_LANGUAGE')
    DB_TYPE = os.getenv('DB_TYPE')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_DATABASE = os.getenv('DB_DATABASE')
    DB_DRIVER = os.getenv('DB_DRIVER')


def get_env() -> ReadEnv:
    return ReadEnv()
