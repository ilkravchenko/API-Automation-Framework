import allure
from httpx import Response

from models.albums import DefaultAlbum, UpdateAlbum
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class AlbumsClient(APIClient):

    @allure.step("Getting all albums.")
    async def get_albums_api(self) -> Response:
        return await self.client.get(APIRoutes.ALBUMS)

    @allure.step("Getting album with id '{album_id}'.")
    async def get_album_api(self, album_id: int) -> Response:
        return await self.client.get(f"{APIRoutes.ALBUMS}/{album_id}")

    @allure.step("Create album")
    async def create_album_api(self, payload: DefaultAlbum) -> Response:
        return await self.client.post(APIRoutes.ALBUMS, json=payload.model_dump(by_alias=True))

    @allure.step("Updating album with id '{album_id}'.")
    async def update_album_api(self, album_id: int, payload: UpdateAlbum) -> Response:
        return await self.client.patch(f"{APIRoutes.ALBUMS}/{album_id}", json=payload.model_dump(by_alias=True))

    @allure.step("Deleting album with id '{album_id}'.")
    async def delete_album_api(self, album_id: int) -> Response:
        return await self.client.delete(f"{APIRoutes.ALBUMS}/{album_id}")

    async def create_album(self, album_id: int) -> DefaultAlbum:
        payload = DefaultAlbum(album_id=album_id)

        response = await self.create_album_api(payload)
        return DefaultAlbum(**response.json())
