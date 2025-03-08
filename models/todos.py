from typing import TypedDict

from faker import Faker
from pydantic import BaseModel, Field

fake = Faker()


class UpdateTodo(BaseModel):
    user_id: int = Field(default_factory=int, alias='userId')
    title: str = Field(default_factory=fake.sentence)
    completed: bool = Field(default_factory=fake.boolean)


class DefaultTodo(BaseModel):
    user_id: int = Field(default_factory=int, alias='userId')
    id: int = Field(default_factory=int)
    title: str = Field(default_factory=fake.sentence)
    completed: bool = Field(default_factory=fake.boolean)


class DefaultTodoList(BaseModel):
    root: list[DefaultTodo]


class TodoDict(TypedDict):
    id: int
    title: str
    completed: bool
    userId: int
