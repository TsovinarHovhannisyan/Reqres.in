import allure
import pytest
import requests

base_url = "https://reqres.in/api"

@allure.feature('User Feature')
@allure.suite('Register User Suite')
@allure.title('Test Register User')
@allure.description('Test to register a user and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_register_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to register a user'):
        response = requests.post(
            f'{base_url}/register',
            json=data,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify "id" is present in response'):
        assert "id" in response_data, "The response does not contain 'id'"

    with allure.step('Verify "token" is present in response'):
        assert "token" in response_data, "The response does not contain 'token'"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)