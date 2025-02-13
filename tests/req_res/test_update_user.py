import requests
import pytest
from assertpy import assert_that
from http import HTTPStatus

name = "morpheus"
job = "zion resident"
user_payload = {
    "name": name,
    "job": job
}

@pytest.fixture(scope="module")
def put_update_request():
    return requests.put("https://reqres.in/api/users/2", json=user_payload)


def test_update_user_status_code(put_update_request):
    print(put_update_request.text)
    assert_that(put_update_request.status_code).is_equal_to(HTTPStatus.OK)


def test_update_reason(put_update_request):
    assert_that(put_update_request.reason).is_equal_to(HTTPStatus.OK.phrase)


def test_update_message(put_update_request):
    assert_that(put_update_request.json()).contains_entry({"name": name})
    assert_that(put_update_request.json()).contains_entry({"job": job})
    assert_that(put_update_request.json()["updatedAt"]).matches(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z")

