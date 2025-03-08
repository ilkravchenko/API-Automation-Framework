from http import HTTPStatus

import allure
import pytest

from base.api.photos_api import PhotosClient
from models.photos import DefaultPhoto, DefaultPhotoList, PhotoDict, UpdatePhoto
from utils.assertions.api.photos import assert_photo
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.photos
@allure.feature('Photos')
@allure.story('Photos API')
class TestPhotos:

    @allure.title("Get Photos")
    async def test_get_photos(self, class_photos_client: PhotosClient):
        response = await class_photos_client.get_photos_api()
        json_response: list[PhotoDict] = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(
            {"root": json_response},
            DefaultPhotoList.model_json_schema()
        )

    @allure.title("Create Photo")
    async def test_create_photo(self, class_photos_client: PhotosClient):
        payload = DefaultPhoto()

        response = await class_photos_client.create_photo_api(payload)
        json_response: PhotoDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_photo(expected_photo=json_response, actual_photo=payload)

        validate_schema(json_response, DefaultPhoto.model_json_schema())

    @allure.title("Get Photo")
    async def test_get_photo(self, random_photo: int, class_photos_client: PhotosClient):
        response = await class_photos_client.get_photo_api(random_photo)
        json_response: PhotoDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultPhoto.model_json_schema())

    @allure.title("Update Photo")
    async def test_update_photo(self, function_photo: DefaultPhoto, class_photos_client: PhotosClient):
        payload = UpdatePhoto()

        response = await class_photos_client.update_photo_api(function_photo.id, payload)
        json_response: PhotoDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_photo(expected_photo=json_response, actual_photo=payload)

        validate_schema(json_response, DefaultPhoto.model_json_schema())

    @allure.title("Delete Photo")
    async def test_delete_photo(self, function_photo: DefaultPhoto, class_photos_client: PhotosClient):
        delete_photo_response = await class_photos_client.delete_photo_api(function_photo.id)
        get_photo_response = await class_photos_client.get_photo_api(function_photo.id)

        assert_status_code(delete_photo_response.status_code, HTTPStatus.OK)
        assert_status_code(get_photo_response.status_code, HTTPStatus.NOT_FOUND)

