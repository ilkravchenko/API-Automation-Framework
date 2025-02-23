from enum import Enum


class APIRoutes(str, Enum):
    AUTH = '/auth'
    POSTS = '/posts'
    COMMENTS = '/comments'
    ALBUMS = '/albums'
    PHOTOS = '/photos'
    TODOS = '/todos'
    USERS = '/users'

    def __str__(self) -> str:
        return self.value
