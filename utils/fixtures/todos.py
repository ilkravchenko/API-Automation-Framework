import asyncio
import random

import pytest_asyncio

from base.api.todos_api import TodoClient
from base.api.users_api import UsersClient
from models.authentication import Authentication
from models.todos import DefaultTodo
from utils.clients.http.builder import get_http_client


@pytest_asyncio.fixture(scope='class')
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='class')
async def class_todos_client(event_loop) -> TodoClient:
    client = await get_http_client(auth=Authentication())
    yield TodoClient(client=client)


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
async def random_todo(class_todos_client: TodoClient) -> int:
    response = await class_todos_client.get_todos_api()
    todos = response.json()
    todo_id = random.choice(todos)
    yield todo_id["id"]


@pytest_asyncio.fixture(scope='function')
async def function_todo(class_todos_client: TodoClient, random_user: int) -> DefaultTodo:
    todo = await class_todos_client.create_todo(user_id=random_user)
    yield todo

    await class_todos_client.delete_todo_api(todo.id)
