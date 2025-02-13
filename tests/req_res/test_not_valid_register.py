import requests
import pytest
from assertpy import assert_that
from http import HTTPStatus

user_payload = {
    "email": "sydney@fife"
}

@pytest.fixture(scope="module")
def post_register_request():
    return requests.post("https://reqres.in/api/register", json=user_payload)


def test_not_valid_register_status_code(post_register_request):
    assert_that(post_register_request.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)


def test_not_valid_register_reason(post_register_request):
    assert_that(post_register_request.reason).is_equal_to(HTTPStatus.BAD_REQUEST.phrase)


def test_not_valid_register_message(post_register_request):
    assert_that(post_register_request.json()).contains_entry({"error": "Missing password"})
