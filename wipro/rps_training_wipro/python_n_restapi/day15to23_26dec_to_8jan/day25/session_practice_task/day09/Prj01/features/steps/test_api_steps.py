import requests

from behave import given, when, then

@given('I have a REST API endpoint "{url}"')
def step_given_api_endpoint(context, url):
    context.url = url

@when("I send a GET request to the endpoint")
def step_when_send_get_request(context):
    context.response = requests.get(context.url)

@then('I should get a {status_code:d} response code')
def step_then_verify_status_code(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain the key "{key}"')
def step_then_verify_response_key(context, key):
    response_json = context.response.json()
    assert key in response_json, f"Key '{key}' not found in response"