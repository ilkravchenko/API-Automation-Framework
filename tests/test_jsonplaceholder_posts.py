from http import HTTPStatus

import allure
import pytest

from base.api.posts_api import PostsClient
from models.posts import DefaultPost, DefaultPostList, PostDict, UpdatePost
from utils.assertions.api.posts import assert_post
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.posts
@allure.feature('Posts')
@allure.story('Posts API')
class TestPosts:
    @allure.title("Get posts")
    async def test_get_posts(self, class_posts_client: PostsClient):
        response = await class_posts_client.get_posts_api()
        json_response: list[PostDict] = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(
            {"root": json_response},
            DefaultPostList.model_json_schema()
        )

    @allure.title("Create post")
    async def test_create_post(self, class_posts_client: PostsClient):
        payload = DefaultPost()

        response = await class_posts_client.create_post_api(payload)
        json_response: PostDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_post(expected_post=json_response, actual_post=payload)

        validate_schema(json_response, DefaultPost.model_json_schema())

    @allure.title("Get post")
    async def test_get_post(self, function_existing_user: int, class_posts_client: PostsClient):
        response = await class_posts_client.get_post_api(function_existing_user)
        json_response: PostDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultPost.model_json_schema())

    @allure.title("Update post")
    async def test_update_post(self, function_post: DefaultPost, class_posts_client: PostsClient):
        payload = UpdatePost()

        response = await class_posts_client.update_post_api(function_post.id, payload)
        json_response: PostDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_post(expected_post=json_response, actual_post=payload)

        validate_schema(json_response, DefaultPost.model_json_schema())

    @allure.title("Delete post")
    async def test_delete_post(self, function_post: DefaultPost, class_posts_client: PostsClient):
        delete_post_response = await class_posts_client.delete_post_api(function_post.id)
        get_post_response = await class_posts_client.get_post_api(function_post.id)

        assert_status_code(delete_post_response.status_code, HTTPStatus.OK)
        assert_status_code(get_post_response.status_code, HTTPStatus.NOT_FOUND)
