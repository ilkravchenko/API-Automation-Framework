from typing import TypedDict

from typing import Dict, Any
from faker import Faker
from pydantic import BaseModel, Field

fake = Faker()


class UpdatePost(BaseModel):
    user_id: int = Field(default_factory=fake.unique.random_int, alias='userId')
    title: str = Field(default_factory=fake.sentence)
    body: str = Field(default_factory=fake.text)


class DefaultPost(BaseModel):
    user_id: int = Field(default_factory=fake.unique.random_int, alias='userId')
    id: int = Field(default_factory=fake.unique.random_int)
    title: str = Field(default_factory=fake.sentence)
    body: str = Field(default_factory=fake.text)

    def exclude_fields(self, exclude_fields: list[str] = None) -> str:
        exclude_fields = set(exclude_fields) if exclude_fields else set()
        return self.model_dump_json(exclude=exclude_fields)

    def modify_fields(self, changes: Dict[str, Any] = None, remove_fields: list[str] = None) -> "DefaultPost":
        data = self.model_dump()

        # Change received fields from changes
        if changes:
            for key, value in changes.items():
                data[key] = value

        # Delete received fields from remove_fields
        if remove_fields:
            for field in remove_fields:
                data.pop(field, None)

        return DefaultPost(**data)


class DefaultPostList(BaseModel):
    root: list[DefaultPost]


class PostDict(TypedDict):
    id: int
    userId: int
    title: str
    body: str
