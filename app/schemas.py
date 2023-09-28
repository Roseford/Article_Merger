from pydantic_settings import BaseSettings
from typing import Any

class Links(BaseSettings):
 link1: list
 link2: list

class Topic(BaseSettings):
 topic: str

class Docs(BaseSettings):
    doc1: str
    doc2: str