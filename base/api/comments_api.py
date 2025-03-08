import allure
from httpx import Response

from models.comments import DefaultComment, UpdateComment
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class CommentsClient(APIClient):

    @allure.step("Getting all comments.")
    async def get_comments_api(self) -> Response:
        return await self.client.get(APIRoutes.COMMENTS)

    @allure.step("Getting comment with id '{comment_id}'.")
    async def get_comment_api(self, comment_id: int) -> Response:
        return await self.client.get(f"{APIRoutes.COMMENTS}/{comment_id}")

    @allure.step("Create comment.")
    async def create_comment_api(self, payload: DefaultComment) -> Response:
        return await self.client.post(APIRoutes.COMMENTS, json=payload.model_dump(by_alias=True))

    @allure.step("Updating comment with id '{comment_id}'.")
    async def update_comment_api(self, comment_id: int, payload: UpdateComment) -> Response:
        return await self.client.patch(f"{APIRoutes.COMMENTS}/{comment_id}", json=payload.model_dump(by_alias=True))

    @allure.step("Deleting comment with id '{comment_id}'.")
    async def delete_comment_api(self, comment_id: int) -> Response:
        return await self.client.delete(f"{APIRoutes.COMMENTS}/{comment_id}")

    async def create_comment(self, post_id: int) -> DefaultComment:
        payload = DefaultComment(post_id=post_id)

        response = await self.create_comment_api(payload)
        return DefaultComment(**response.json())
