from models.posts import DefaultPost, UpdatePost, PostDict
from utils.assertions.base.expect import expect


def assert_post(expected_post: PostDict, actual_post: DefaultPost | UpdatePost):
    expect(expected_post["user_id"]) \
        .set_description("Post 'userId'") \
        .to_be_equal(actual_post.user_id)

    expect(expected_post["title"]) \
        .set_description("Post 'title'") \
        .to_be_equal(actual_post.title)

    expect(expected_post["body"]) \
        .set_description("Post 'body'") \
        .to_be_equal(actual_post.body)
