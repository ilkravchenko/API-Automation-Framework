import allure
from httpx import Response

from models.posts import DefaultPost, UpdatePost
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class PostsClient(APIClient):

    @allure.step("Getting all posts")
    async def get_posts_api(self) -> Response:
        return await self.client.get(APIRoutes.POSTS)

    @allure.step("Getting post with id '{post_id}'")
    async def get_post_api(self, post_id: int) -> Response:
        return await self.client.get(f"{APIRoutes.POSTS}/{post_id}")

    @allure.step("Creating post")
    async def create_post_api(self, payload: DefaultPost) -> Response:
        return await self.client.post(APIRoutes.POSTS, json=payload.model_dump(by_alias=True))

    @allure.step("Updating post with id '{post_id}'")
    async def update_post_api(self, post_id: int, payload: UpdatePost) -> Response:
        return await self.client.patch(f"{APIRoutes.POSTS}/{post_id}", json=payload.model_dump(by_alias=True))

    @allure.step("Deleting post with id '{post_id}'")
    async def delete_post_api(self, post_id: int) -> Response:
        return await self.client.delete(f"{APIRoutes.POSTS}/{post_id}")

    async def create_post(self, user_id: int) -> DefaultPost:
        payload = DefaultPost(user_id=user_id)

        response = await self.create_post_api(payload)
        return DefaultPost(**response.json())
