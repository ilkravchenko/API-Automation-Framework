import asyncio
import random

import pytest_asyncio

from base.api.posts_api import PostsClient
from base.api.users_api import UsersClient
from models.authentication import Authentication
from models.posts import DefaultPost
from utils.clients.http.builder import get_http_client


@pytest_asyncio.fixture(scope="class")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="class")
async def class_posts_client(event_loop) -> PostsClient:
    client = await get_http_client(auth=Authentication())
    yield PostsClient(client=client)


@pytest_asyncio.fixture(scope="class")
async def class_users_client(event_loop) -> UsersClient:
    client = await get_http_client(auth=Authentication())
    yield UsersClient(client=client)


@pytest_asyncio.fixture(scope='function')
async def random_user(class_users_client: UsersClient) -> int:
    response = await class_users_client.get_users_api()
    users = response.json()
    user_id = random.choice(users)
    yield user_id["id"]


@pytest_asyncio.fixture(scope='function')
async def function_post(class_posts_client: PostsClient, random_user: int) -> DefaultPost:
    post = await class_posts_client.create_post(user_id=random_user)
    yield post

    await class_posts_client.delete_post_api(post.id)
