from models.albums import DefaultAlbum, UpdateAlbum, AlbumDict
from utils.assertions.base.expect import expect


def assert_album(expected_album: AlbumDict, actual_album: DefaultAlbum | UpdateAlbum):
    expect(expected_album['userId']) \
        .set_description("Album 'userId'") \
        .to_be_equal(actual_album.user_id)

    expect(expected_album['title']) \
        .set_description("Album 'title'") \
        .to_be_equal(actual_album.title)
