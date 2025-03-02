from typing import TypedDict

from faker import Faker
from pydantic import BaseModel, Field

fake = Faker()


class UpdatePost(BaseModel):
    user_id: int = Field(default_factory=int)
    id: int = Field(default_factory=fake.unique.random_int)
    title: str = Field(default_factory=fake.sentence)
    body: str = Field(default_factory=fake.text)


class DefaultPost(BaseModel):
    user_id: int = Field(default_factory=int)
    id: int = Field(default_factory=fake.unique.random_int)
    title: str = Field(default_factory=fake.sentence)
    body: str = Field(default_factory=fake.text)


class DefaultPostList(BaseModel):
    root: list[DefaultPost]


class PostDict(TypedDict):
    id: int
    user_id: int
    title: str
    body: str
