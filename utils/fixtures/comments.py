import asyncio
import random

import pytest_asyncio

from base.api.comments_api import CommentsClient
from base.api.posts_api import PostsClient
from models.authentication import Authentication
from models.comments import DefaultComment
from utils.clients.http.builder import get_http_client


@pytest_asyncio.fixture(scope='class')
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='class')
async def class_comments_client(event_loop) -> CommentsClient:
    client = await get_http_client(auth=Authentication())
    yield CommentsClient(client=client)


@pytest_asyncio.fixture(scope='class')
async def class_posts_client(event_loop) -> PostsClient:
    client = await get_http_client(auth=Authentication())
    yield PostsClient(client=client)


@pytest_asyncio.fixture(scope='function')
async def random_post(class_posts_client: PostsClient) -> int:
    response = await class_posts_client.get_posts_api()
    posts = response.json()
    post_id = random.choice(posts)
    yield post_id["id"]


@pytest_asyncio.fixture(scope='function')
async def function_comment(class_comments_client: CommentsClient, random_post: int) -> DefaultComment:
    comment = await class_comments_client.create_comment(comment_id=random_post)
    yield comment

    await class_comments_client.delete_comment_api(comment.id)
