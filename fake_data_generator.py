import sys

from typing import Optional
import pandas as pd
from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from read_env import get_env
from mount_fake import mount_fake
from tqdm import tqdm

env = get_env()


class FakeDataGenerator:
    def __init__(
        self,
        config: dict,
        db_type: str,
        db_host: str,
        db_port: str,
        db_user: str,
        db_password: str,
        db_database: str,
        db_driver: Optional[str] = None
    ) -> None:
        self.config = config
        self.db_type = db_type
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_password = db_password
        self.db_database = db_database
        self.db_driver = db_driver
        self.faker = Faker(env.FAKER_LANGUAGE or None)

    def __call__(self) -> bool:
        engine = create_engine(self.__mount_connection_string())
        schemas = self.config["config"]["schemas"]

        Session = sessionmaker(bind=engine)

        for schema in schemas:
            tables = schema["tables"]

            for table in tables:
                print("Mount Table: ", table["name"])
                data = self.__mount_data(table["data_model"], table["data_count"])

                df = pd.DataFrame.from_dict(data)

                with Session() as session:
                    try:
                        df.to_sql(
                            table["name"],
                            con=engine,
                            schema=schema["schema_used"],
                            if_exists="append",
                            index=False
                        )

                        session.commit()

                    except Exception as err:
                        print(err, "Ocorreu um erro, vamos dar rowback no banco!")
                        session.rollback()

                    finally:
                        session.close()

    def __mount_data(self, table_info, data_count):
        for table_name in table_info:
            print(f"Mount Column: {table_name}")
            table_info[table_name] = [
                mount_fake(self.faker, table_info[table_name])
                for _ in tqdm(range(data_count))
            ]

            print("\n")
        print("\n\n")

        return table_info

    def __mount_connection_string(self) -> Engine:
        db_types = [
            (
                "mssql+pyodbc",
                f"mssql+pyodbc://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_database}?driver={self.db_driver}"

            ),
            (
                "postgresql+psycopg2",
                f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_database}"
            ),
            (
                "mysql+pymysql",
                f'mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_database}'
            )
        ]

        connection_string = list(filter(
            lambda x: x[0] == self.db_type, db_types
        ))

        # TODO: use customer error here
        if not connection_string:
            raise FileExistsError

        return connection_string[0][1]
