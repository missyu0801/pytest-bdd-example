from pytest_bdd import scenarios, given, when, then, parsers
import requests
import pytest
import json
from utilities import configurations

scenarios("../feature/api.feature")


@given(parsers.parse("the API endpoint {url}"), target_fixture="endpoint")
def endpoint(url):
    print(url)
    return url

@pytest.fixture()
@when('I perform a GET request')
def perform_get(endpoint):
    request = requests.get(endpoint)
    print(request.content)
    return request

@when(parsers.parse("I input a json '{path}' file"))
def input_jsonfile(path):
    with open(path) as f:
        json_request = json.loads(f.read())
    return json_request


@when('I perform a POST request')
def perform_post(endpoint, input_jsonfile):
    request = requests.post(endpoint, json=input_jsonfile)
    print(request.content)
    return request

@then(parsers.parse("the response code for the GET request should be {status_code:d}"))
def check_response_code(perform_get, status_code):
    assert perform_get.status_code == int(status_code)



