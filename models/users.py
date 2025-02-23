from typing import TypedDict

from pydantic import BaseModel, Field
from faker import Faker

fake = Faker()


class DefaultGeo(BaseModel):
    lat: str = Field(default_factory=lambda: str(fake.latitude()))
    lng: str = Field(default_factory=lambda: str(fake.longitude()))


class DefaultAddress(BaseModel):
    street: str = Field(default_factory=fake.street_address)
    suite: str = Field(default_factory=fake.secondary_address)
    city: str = Field(default_factory=fake.city)
    zipcode: str = Field(default_factory=fake.zipcode)
    geo: DefaultGeo = Field(default_factory=DefaultGeo)


class DefaultCompany(BaseModel):
    name: str = Field(default_factory=fake.company)
    catch_phrase: str = Field(alias="catchPhrase", default_factory=fake.catch_phrase)
    bs: str = Field(default_factory=fake.bs)


class DefaultUser(BaseModel):
    id: int = Field(default_factory=fake.unique.random_int)
    name: str = Field(default_factory=fake.name)
    username: str = Field(default_factory=fake.user_name)
    email: str = Field(default_factory=fake.email)
    address: DefaultAddress = Field(default_factory=DefaultAddress)
    phone: str = Field(default_factory=fake.phone_number)
    website: str = Field(default_factory=fake.safe_domain_name)
    company: DefaultCompany = Field(default_factory=DefaultCompany)


class UpdateUser(BaseModel):
    name: str = Field(default_factory=fake.name)
    username: str = Field(default_factory=fake.user_name)
    email: str = Field(default_factory=fake.email)
    address: DefaultAddress = Field(default_factory=DefaultAddress)
    phone: str = Field(default_factory=fake.phone_number)
    website: str = Field(default_factory=fake.safe_domain_name)
    company: DefaultCompany = Field(default_factory=DefaultCompany)


class DefaultUsersList(BaseModel):
    root: list[DefaultUser]


class GeoDict(TypedDict):
    lat: str
    lng: str


class AddressDict(TypedDict):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoDict


class CompanyDict(TypedDict):
    name: str
    catchPhrase: str
    bs: str


class UserDict(TypedDict):
    id: int
    name: str
    username: str
    email: str
    address: AddressDict
    phone: str
    website: str
    company: CompanyDict
