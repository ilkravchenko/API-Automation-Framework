from http import HTTPStatus

import allure
import pytest

from base.api.albums_api import AlbumsClient
from models.albums import AlbumDict, DefaultAlbum, DefaultAlbumList, UpdateAlbum
from utils.assertions.api.albums import assert_album
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.albums
@allure.feature('Albums')
@allure.story('Albums API')
class TestAlbums:

    @allure.title("Get Albums")
    async def test_get_albums(self, class_albums_client: AlbumsClient):
        response = await class_albums_client.get_albums_api()
        json_response: list[DefaultAlbum] = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema({
            "root": json_response
        }, DefaultAlbumList.model_json_schema())

    @allure.title("Create Album")
    async def test_create_album(self, class_albums_client: AlbumsClient):
        payload: DefaultAlbum = DefaultAlbum()

        response = await class_albums_client.create_album_api(payload)
        json_response: AlbumDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_album(expected_album=json_response, actual_album=payload)

        validate_schema(json_response, DefaultAlbum.model_json_schema())

    @allure.title("Get Album")
    async def test_get_album(self, random_album: int, class_albums_client: AlbumsClient):
        response = await class_albums_client.get_album_api(random_album)
        json_response: AlbumDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultAlbum.model_json_schema())

    @allure.title("Update Album")
    async def test_update_album(self, function_album: DefaultAlbum, class_albums_client: AlbumsClient):
        payload: UpdateAlbum = UpdateAlbum()

        response = await class_albums_client.update_album_api(function_album.id, payload)
        json_response: AlbumDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_album(expected_album=json_response, actual_album=payload)

        validate_schema(json_response, DefaultAlbum.model_json_schema())

    @allure.title("Delete Album")
    async def test_delete_album(self, function_album: DefaultAlbum, class_albums_client: AlbumsClient):
        delete_album_response = await class_albums_client.delete_album_api(function_album.id)
        get_album_response = await class_albums_client.get_album_api(function_album.id)

        assert_status_code(delete_album_response.status_code, HTTPStatus.OK)
        assert_status_code(get_album_response.status_code, HTTPStatus.NOT_FOUND)
