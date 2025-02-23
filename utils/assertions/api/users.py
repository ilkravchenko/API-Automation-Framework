from models.users import DefaultUser, UserDict, UpdateUser
from utils.assertions.base.expect import expect


def assert_user(
        expected_user: UserDict,
        actual_user: DefaultUser | UpdateUser
):
    expect(expected_user["name"]) \
        .set_description("User 'name'") \
        .to_be_equal(actual_user.name)

    expect(expected_user["username"]) \
        .set_description("User 'username'") \
        .to_be_equal(actual_user.username)

    expect(expected_user["email"]) \
        .set_description("User 'email'") \
        .to_equal(actual_user.email)

    expect(expected_user["address"]) \
        .set_description("User 'address'") \
        .to_be_equal(actual_user.address.model_dump())

    expect(expected_user["address"]["street"]) \
        .set_description("User 'address.street'") \
        .to_be_equal(actual_user.address.street)

    expect(expected_user["address"]["suite"]) \
        .set_description("User 'address.suite'") \
        .to_be_equal(actual_user.address.suite)

    expect(expected_user["address"]["city"]) \
        .set_description("User 'address.city'") \
        .to_be_equal(actual_user.address.city)

    expect(expected_user["address"]["zipcode"]) \
        .set_description("User 'address.zipcode'") \
        .to_be_equal(actual_user.address.zipcode)

    expect(expected_user["address"]["geo"]) \
        .set_description("User 'address.geo'") \
        .to_be_equal(actual_user.address.geo.model_dump())

    expect(expected_user["address"]["geo"]["lat"]) \
        .set_description("User 'address.geo.lat'") \
        .to_be_equal(actual_user.address.geo.lat)

    expect(expected_user["address"]["geo"]["lng"]) \
        .set_description("User 'address.geo.lng'") \
        .to_be_equal(actual_user.address.geo.lng)

    expect(expected_user["phone"]) \
        .set_description("User 'phone'") \
        .to_be_equal(actual_user.phone)

    expect(expected_user["website"]) \
        .set_description("User 'website'") \
        .to_be_equal(actual_user.phone)

    expect(expected_user["company"]) \
        .set_description("User 'company'") \
        .to_be_equal(actual_user.company.model_dump())

    expect(expected_user["company"]["name"]) \
        .set_description("User 'company.name'") \
        .to_be_equal(actual_user.company.name)

    expect(expected_user["company"]["catchPhrase"]) \
        .set_description("User 'company.catchPhrase'") \
        .to_be_equal(actual_user.company.catch_phrase)

    expect(expected_user["company"]["bs"]) \
        .set_description("User 'company.bs'") \
        .to_be_equal(actual_user.company.bs)
