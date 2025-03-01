from http import HTTPStatus

import allure
import pytest

from base.api.users_api import UsersClient
from models.users import DefaultUser, DefaultUsersList, UpdateUser, UserDict
from utils.assertions.api.users import assert_user
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.users
@allure.feature('Test Users')
@allure.story('Test Users API')
class TestUsers:

    @allure.title("Get users")
    async def test_get_users(self, class_users_client: UsersClient):
        response = await class_users_client.get_users_api()
        json_response: list[UserDict] = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema({
            "root": json_response
        }, DefaultUsersList.model_json_schema())

    @allure.title('Create user')
    async def test_create_user(self, class_users_client: UsersClient):
        payload = DefaultUser()

        response = await class_users_client.create_user_api(payload)
        json_response: UserDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_user(expected_user=json_response, actual_user=payload)

        validate_schema(json_response, DefaultUser.model_json_schema())

    @allure.title('Get user')
    async def test_get_user(self, function_existing_user: int, class_users_client: UsersClient):
        response = await class_users_client.get_user_api(function_existing_user)
        json_response: UserDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultUser.model_json_schema())

    @allure.title('Update user')
    async def test_update_user(self, function_user: DefaultUser, class_users_client: UsersClient):
        payload = UpdateUser()

        response = await class_users_client.update_user_api(function_user.id, payload)
        json_response: UserDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_user(expected_user=json_response, actual_user=payload)

        validate_schema(json_response, DefaultUser.model_json_schema())

    @allure.title('Delete user')
    async def test_delete_user(self, function_user: DefaultUser, class_users_client: UsersClient):
        delete_question_response = await class_users_client.delete_user_api(function_user.id)
        get_question_response = await class_users_client.get_user_api(function_user.id)

        assert_status_code(delete_question_response.status_code, HTTPStatus.OK)
        assert_status_code(get_question_response.status_code, HTTPStatus.NOT_FOUND)
