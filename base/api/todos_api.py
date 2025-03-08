import allure
from httpx import Response

from models.todos import DefaultTodo, UpdateTodo
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class TodoClient(APIClient):

    @allure.step("Getting all todos.")
    async def get_todos_api(self) -> Response:
        return await self.client.get(APIRoutes.TODOS)

    @allure.step("Getting todo with id 'todo_id'.")
    async def get_todo_api(self, todo_id: int) -> Response:
        return await self.client.get(f"{APIRoutes.TODOS}/{todo_id}")

    @allure.step("Create todo.")
    async def create_todo_api(self, payload: DefaultTodo) -> Response:
        return await self.client.post(APIRoutes.TODOS, json=payload.model_dump(by_alias=True))

    @allure.step("Updating todo with id 'todo_id'.")
    async def update_todo_api(self, todo_id: int, payload: UpdateTodo) -> Response:
        return await self.client.patch(f"{APIRoutes.TODOS}/{todo_id}", json=payload.model_dump(by_alias=True))

    @allure.step("Deleting todo with id 'todo_id'.")
    async def delete_todo_api(self, todo_id: int) -> Response:
        return await self.client.delete(f"{APIRoutes.TODOS}/{todo_id}")

    async def create_todo(self, user_id: int) -> DefaultTodo:
        payload = DefaultTodo(user_id=user_id)

        response = await self.create_todo_api(payload)
        return DefaultTodo(**response.json())
