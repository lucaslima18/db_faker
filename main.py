##!/usr/bin/python
from fake_data_generator import FakeDataGenerator
from read_env import get_env
from read_config import get_config

env = get_env()

if __name__ == '__main__':
    FakeDataGenerator(
        config=get_config(),
        db_type=env.DB_TYPE,
        db_host=env.DB_HOST,
        db_port=env.DB_PORT,
        db_user=env.DB_USER,
        db_password=env.DB_PASSWORD,
        db_database=env.DB_DATABASE,
        db_driver=env.DB_DRIVER
    )()
