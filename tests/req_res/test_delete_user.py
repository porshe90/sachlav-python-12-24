import requests
from assertpy import assert_that
from http import HTTPStatus




def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2")
    assert_that(response.status_code).is_equal_to(HTTPStatus.NO_CONTENT)
    assert_that(response.reason).is_equal_to(HTTPStatus.NO_CONTENT.phrase)
    assert_that(response.text).is_empty()