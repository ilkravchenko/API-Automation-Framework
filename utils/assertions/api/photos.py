from models.photos import DefaultPhoto, PhotoDict, UpdatePhoto
from utils.assertions.base.expect import expect


def assert_photo(expected_photo: PhotoDict, actual_photo: DefaultPhoto | UpdatePhoto):
    expect(expected_photo["albumId"]) \
        .set_description("Photo 'albumId'") \
        .to_be_equal(actual_photo.album_id)

    expect(expected_photo["title"]) \
        .set_description("Photo 'title'") \
        .to_be_equal(actual_photo.title)

    expect(expected_photo["url"]) \
        .set_description("Photo 'url'") \
        .to_be_equal(actual_photo.url)

    expect(expected_photo["thumbnailUrl"]) \
        .set_description("Photo 'thumbnailUrl'") \
        .to_be_equal(actual_photo.thumbnail_url)
