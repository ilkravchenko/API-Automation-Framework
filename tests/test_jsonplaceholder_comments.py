from http import HTTPStatus

import allure
import pytest

from base.api.comments_api import CommentsClient
from models.comments import CommentDict, DefaultComment, DefaultCommentList, UpdateComment
from utils.assertions.api.comments import assert_comment
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.comments
@allure.feature('Comments')
@allure.story('Comments API')
class TestComments:

    @allure.title('Get Comments')
    async def test_get_comments(self, class_comments_client: CommentsClient):
        response = await class_comments_client.get_comments_api()
        json_response: list[CommentDict] = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(
            {"root": json_response},
            DefaultCommentList.model_json_schema()
        )

    @allure.title('Create comment')
    async def test_create_comment(self, class_comments_client: CommentsClient):
        payload = DefaultComment()

        response = await class_comments_client.create_comment_api(payload)
        json_response: CommentDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_comment(expected_comment=json_response, actual_comment=payload)

        validate_schema(json_response, DefaultComment.model_json_schema())

    @allure.title('Get comment')
    async def test_get_comment(self, random_comment: int, class_comments_client: CommentsClient):
        response = await class_comments_client.get_comment_api(random_comment)
        json_response: CommentDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultComment.model_json_schema())

    @allure.title('Update comment')
    async def test_update_comment(self, function_comment: DefaultComment, class_comments_client: CommentsClient):
        payload = UpdateComment()

        response = await class_comments_client.update_comment_api(function_comment.id, payload)
        json_response: CommentDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_comment(expected_comment=json_response, actual_comment=payload)

        validate_schema(json_response, DefaultComment.model_json_schema())

    @allure.title('Delete comment')
    async def test_delete_comment(self, function_comment: DefaultComment, class_comments_client: CommentsClient):
        delete_comment_response = await class_comments_client.delete_comment_api(function_comment.id)
        get_comment_response = await class_comments_client.get_comment_api(function_comment.id)

        assert_status_code(delete_comment_response.status_code, HTTPStatus.OK)
        assert_status_code(get_comment_response.status_code, HTTPStatus.NOT_FOUND)
