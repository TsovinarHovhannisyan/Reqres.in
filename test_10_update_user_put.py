import allure
import pytest
import requests

base_url = "https://reqres.in/api"
user_id = 2

@allure.feature('User Feature')
@allure.suite('Update User Suite')
@allure.title('Test Update User')
@allure.description('Test to update a user and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send PUT request to update a user'):
        response = requests.put(
            f'{base_url}/users/{user_id}',
            json=data,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify "name" is correct'):
        assert response_data['name'] == data['name'], f"Expected name to be {data['name']} but got '{response_data['name']}'"

    with allure.step('Verify "job" is correct'):
        assert response_data['job'] == data['job'], f"Expected job to be {data['job']} but got '{response_data['job']}'"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)