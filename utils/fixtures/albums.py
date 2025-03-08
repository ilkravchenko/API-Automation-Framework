import asyncio
import random

import pytest_asyncio

from base.api.albums_api import AlbumsClient
from base.api.users_api import UsersClient
from models.authentication import Authentication
from models.albums import DefaultAlbum
from utils.clients.http.builder import get_http_client


@pytest_asyncio.fixture(scope='class')
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='class')
async def class_albums_client(event_loop) -> AlbumsClient:
    client = await get_http_client(auth=Authentication())
    yield AlbumsClient(client=client)


@pytest_asyncio.fixture(scope='class')
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
async def random_album(class_albums_client: AlbumsClient) -> int:
    response = await class_albums_client.get_albums_api()
    albums = response.json()
    album_id = random.choice(albums)
    yield album_id["id"]


@pytest_asyncio.fixture(scope='function')
async def function_album(class_albums_client: AlbumsClient, random_user: int) -> DefaultAlbum:
    album = await class_albums_client.create_album(album_id=random_user)
    yield album

    await class_albums_client.delete_album_api(album.id)
