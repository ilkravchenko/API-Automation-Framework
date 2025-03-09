from models.posts import DefaultPost, PostDict, UpdatePost
from utils.assertions.base.expect import expect


def assert_post(expected_post: PostDict, actual_post: DefaultPost | UpdatePost):
    expect(expected_post["userId"]) \
        .set_description("Post 'userId'") \
        .to_be_equal(actual_post.user_id)

    expect(expected_post["title"]) \
        .set_description("Post 'title'") \
        .to_be_equal(actual_post.title)

    expect(expected_post["body"]) \
        .set_description("Post 'body'") \
        .to_be_equal(actual_post.body)


def assert_post_empty_error(expected_error: dict, actual_error: dict, field: str):
    expect(expected_error) \
        .set_description(f"Post 'error' while empty required field '{field}'") \
        .to_be_equal(actual_error)


def assert_post_without_field(expected_error: dict, actual_error: dict, field: str):
    expect(expected_error) \
        .set_description(f"Post 'error' while not found required field '{field}'") \
        .to_be_equal(actual_error)


def assert_post_with_invalid_field(expected_error: dict, actual_error: dict, field: str):
    expect(expected_error) \
        .set_description(f"Post 'error' while provided invalid field '{field}'") \
        .to_be_equal(actual_error)
