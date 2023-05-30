from pydantic import BaseModel
from typing import Dict, Any, List
import json


class TableMountInfo(BaseModel):
    name: str
    data_count: int
    data_model: Dict[str, Any]


class DatabaseMountInfo(BaseModel):
    schema_used: str
    tables: List[TableMountInfo]


class Config(BaseModel):
    config: DatabaseMountInfo


def get_config() -> Config:
    with open('config.json', 'r') as config_json:
        return Config(config=json.load(config_json)).dict()
