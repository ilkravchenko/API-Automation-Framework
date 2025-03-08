from typing import TypedDict

from faker import Faker
from pydantic import BaseModel, Field

fake = Faker()


class UpdateComment(BaseModel):
    post_id: int = Field(default_factory=int, alias="postId")
    name: str = Field(default_factory=fake.name)
    email: str = Field(default_factory=fake.email)
    body: str = Field(default_factory=fake.text)


class DefaultComment(BaseModel):
    post_id: int = Field(default_factory=int, alias="postId")
    id: int = Field(default_factory=fake.unique.random_int)
    name: str = Field(default_factory=fake.name)
    email: str = Field(default_factory=fake.email)
    body: str = Field(default_factory=fake.text)


class DefaultCommentList(BaseModel):
    root: list[DefaultComment]


class CommentDict(TypedDict):
    id: int
    postId: int
    name: str
    email: str
    body: str
