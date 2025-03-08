from models.comments import CommentDict, DefaultComment, UpdateComment
from utils.assertions.base.expect import expect


def assert_comment(expected_comment: CommentDict, actual_comment: DefaultComment | UpdateComment):
    expect(expected_comment["postId"]) \
        .set_description("Comment 'postId'") \
        .to_be_equal(actual_comment.post_id)

    expect(expected_comment["name"]) \
        .set_description("Comment 'name'") \
        .to_be_equal(actual_comment.name)

    expect(expected_comment["email"]) \
        .set_description("Comment 'email'") \
        .to_be_equal(actual_comment.email)

    expect(expected_comment["body"]) \
        .set_description("Comment 'body'") \
        .to_be_equal(actual_comment.body)
