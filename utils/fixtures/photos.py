import asyncio
import random

import pytest_asyncio

from base.api.albums_api import AlbumsClient
from base.api.photos_api import PhotosClient
from models.authentication import Authentication
from models.photos import DefaultPhoto
from utils.clients.http.builder import get_http_client


@pytest_asyncio.fixture(scope='class')
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='class')
async def class_photos_client(event_loop) -> PhotosClient:
    client = await get_http_client(auth=Authentication())
    yield PhotosClient(client=client)


@pytest_asyncio.fixture(scope='class')
async def class_albums_client(event_loop) -> AlbumsClient:
    client = await get_http_client(auth=Authentication())
    yield AlbumsClient(client=client)


@pytest_asyncio.fixture(scope='function')
async def random_album(class_albums_client: AlbumsClient) -> int:
    response = await class_albums_client.get_albums_api()
    albums = response.json()
    album_id = random.choice(albums)
    yield album_id["id"]


@pytest_asyncio.fixture(scope='function')
async def random_photo(class_photos_client: PhotosClient) -> int:
    response = await class_photos_client.get_photos_api()
    photos = response.json()
    photo_id = random.choice(photos)
    yield photo_id["id"]


@pytest_asyncio.fixture(scope='function')
async def function_photo(class_photos_client: PhotosClient, random_album: int) -> DefaultPhoto:
    photo = await class_photos_client.create_photo(album_id=random_album)
    yield photo

    await class_photos_client.delete_photo_api(photo.id)
