import asyncio
import random
import pytest_asyncio

from base.api.users_api import UsersClient
from models.authentication import Authentication
from models.users import DefaultUser
from utils.clients.http.builder import get_http_client


@pytest_asyncio.fixture(scope="class")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="class")
async def class_users_client(event_loop) -> UsersClient:
    client = await get_http_client(auth=Authentication())
    yield UsersClient(client=client)


@pytest_asyncio.fixture(scope='function')
async def function_user(class_users_client: UsersClient) -> DefaultUser:
    user = await class_users_client.create_user()
    yield user

    await class_users_client.delete_user_api(user.id)


@pytest_asyncio.fixture(scope="function")
def function_existing_user():
    yield random.randint(1, 10)
