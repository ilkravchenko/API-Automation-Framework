from typing import TypedDict

from faker import Faker
from pydantic import BaseModel, Field

fake = Faker()


class UpdateAlbum(BaseModel):
    user_id: int = Field(default_factory=int, alias='userId')
    title: str = Field(default_factory=fake.sentence, alias='title')


class DefaultAlbum(BaseModel):
    user_id: int = Field(default_factory=int, alias='userId')
    id: int = Field(default_factory=int)
    title: str = Field(default_factory=fake.sentence)


class DefaultAlbumList(BaseModel):
    root: list[DefaultAlbum]


class AlbumDict(TypedDict):
    userId: int
    id: int
    title: str
