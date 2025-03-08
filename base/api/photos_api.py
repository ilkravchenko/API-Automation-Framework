import allure
from httpx import Response

from models.photos import DefaultPhoto, UpdatePhoto
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class PhotosClient(APIClient):

    @allure.step("Getting all photos.")
    async def get_photos_api(self) -> Response:
        return await self.client.get(APIRoutes.PHOTOS)

    @allure.step("Getting photo with id '{photo_id}'.")
    async def get_photo_api(self, photo_id: int) -> Response:
        return await self.client.get(f"{APIRoutes.PHOTOS}/{photo_id}")

    @allure.step("Create photo.")
    async def create_photo_api(self, payload: DefaultPhoto) -> Response:
        return await self.client.post(APIRoutes.PHOTOS, json=payload.model_dump(by_alias=True))

    @allure.step("Updating photo with id '{photo_id}'.")
    async def update_photo_api(self, photo_id: int, payload: UpdatePhoto) -> Response:
        return await self.client.patch(f"{APIRoutes.PHOTOS}/{photo_id}", json=payload.model_dump(by_alias=True))

    @allure.step("Deleting photo with id '{photo_id}'.")
    async def delete_photo_api(self, photo_id: int) -> Response:
        return await self.client.delete(f"{APIRoutes.PHOTOS}/{photo_id}")

    async def create_photo(self, album_id) -> DefaultPhoto:
        payload = DefaultPhoto(album_id=album_id)

        response = await self.create_photo_api(payload)
        return DefaultPhoto(**response.json())
