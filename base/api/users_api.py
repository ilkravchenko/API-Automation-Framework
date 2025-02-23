import allure
from httpx import Response

from models.users import DefaultUser, UpdateUser
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class UsersClient(APIClient):
    @allure.step("Getting all users.")
    async def get_users_api(self) -> Response:
        return await self.client.get(APIRoutes.USERS)

    @allure.step("Getting user with id '{user_id}'.")
    async def get_user_api(self, user_id: int) -> Response:
        return await self.client.get(f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Creating user.")
    async def create_user_api(self, payload: DefaultUser) -> Response:
        return await self.client.post(APIRoutes.USERS, json=payload.model_dump(by_alias=True))

    @allure.step("Updating user with id '{user_id}'.")
    async def update_user_api(self, user_id: int, payload: UpdateUser) -> Response:
        return await self.client.patch(
            f"{APIRoutes.USERS}/{user_id}",
            json=payload.model_dump(by_alias=True)
        )

    @allure.step("Deleting user with id '{user_id}'.")
    async def delete_user_api(self, user_id: int) -> Response:
        return await self.client.delete(f"{APIRoutes.USERS}/{user_id}")

    async def create_user(self) -> DefaultUser:
        payload = DefaultUser()

        response = await self.create_user_api(payload)
        return DefaultUser(**response.json())
