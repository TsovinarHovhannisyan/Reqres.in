import allure
import pytest
import requests

base_url = "https://reqres.in/api"

@allure.feature('User Feature')
@allure.suite('Login User Suite')
@allure.title('Test Login User Missing Password')
@allure.description('Test to login a user with missing password and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_login_user_missing_password():
    data = {
        "email": "peter@klaven"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to login a user with missing password'):
        response = requests.post(
            f'{base_url}/login',
            json=data,
            headers=headers
        )

    with allure.step('Verify response status code is 400'):
        assert response.status_code == 400, f'Expected Status Code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify "error" is present in response'):
        assert "error" in response_data, "The response does not contain 'error'"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)