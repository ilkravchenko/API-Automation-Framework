from http import HTTPStatus

import allure
import pytest

from base.api.todos_api import TodoClient
from models.todos import DefaultTodo, DefaultTodoList, TodoDict, UpdateTodo
from utils.assertions.api.todos import assert_todo
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.todos
@allure.feature('Comments')
@allure.story('Comments API')
class TestTodos:

    @allure.title("Get Todod")
    async def test_get_todos(self, class_todos_client: TodoClient):
        response = await class_todos_client.get_todos_api()
        json_response: list[TodoDict] = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(
            {"root": json_response},
            DefaultTodoList.model_json_schema(),
        )

    @allure.title("Create Todo")
    async def test_create_todo(self, class_todos_client: TodoClient):
        payload = DefaultTodo()

        response = await class_todos_client.create_todo_api(payload)
        json_response: TodoDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_todo(expected_todo=json_response, actual_todo=payload)

        validate_schema(json_response, DefaultTodo.model_json_schema())

    @allure.title("Get Todo")
    async def test_get_todo(self, random_todo: int, class_todos_client: TodoClient):
        response = await class_todos_client.get_todo_api(random_todo)
        json_response: TodoDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultTodo.model_json_schema())

    @allure.title("Update Todo")
    async def test_update_todo(self, function_todo: DefaultTodo, class_todos_client: TodoClient):
        payload = UpdateTodo()

        response = await class_todos_client.update_todo_api(function_todo.id, payload)
        json_response: TodoDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_todo(expected_todo=json_response, actual_todo=payload)

        validate_schema(json_response, DefaultTodo.model_json_schema())

    @allure.title("Delete Todo")
    async def test_delete_todo(self, function_todo: DefaultTodo, class_todos_client: TodoClient):
        delete_todo_response = await class_todos_client.delete_todo_api(function_todo.id)
        get_todo_response = await class_todos_client.get_todo_api(function_todo.id)

        assert_status_code(delete_todo_response.status_code, HTTPStatus.OK)
        assert_status_code(get_todo_response.status_code, HTTPStatus.NOT_FOUND)
