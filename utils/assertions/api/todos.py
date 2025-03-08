from models.todos import DefaultTodo, TodoDict, UpdateTodo
from utils.assertions.base.expect import expect


def assert_todo(expected_todo: TodoDict, actual_todo: DefaultTodo | UpdateTodo):
    expect(expected_todo["userId"]) \
        .set_description("Todo 'userId'") \
        .to_be_equal(actual_todo.user_id)

    expect(expected_todo["title"]) \
        .set_description("Todo 'title'") \
        .to_be_equal(actual_todo.title)

    expect(expected_todo["completed"]) \
        .set_description("Todo 'completed'") \
        .to_be_equal(actual_todo.completed)
