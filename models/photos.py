from typing import TypedDict

from faker import Faker
from pydantic import BaseModel, Field

fake = Faker()


class UpdatePhoto(BaseModel):
    album_id: int = Field(default_factory=int, alias='albumId')
    title: str = Field(default_factory=fake.sentence)
    url: str = Field(default_factory=fake.url)
    thumbnail_url: str = Field(default_factory=fake.url, alias="thumbnailUrl")


class DefaultPhoto(BaseModel):
    album_id: int = Field(default_factory=int, alias='albumId')
    id: int = Field(default_factory=int)
    title: str = Field(default_factory=fake.sentence)
    url: str = Field(default_factory=fake.url)
    thumbnail_url: str = Field(default_factory=fake.url, alias="thumbnailUrl")


class DefaultPhotoList(BaseModel):
    root: list[DefaultPhoto]


class PhotoDict(TypedDict):
    id: int
    albumId: int
    title: str
    url: str
    thumbnailUrl: str
