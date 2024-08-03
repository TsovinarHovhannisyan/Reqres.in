import allure
import pytest
import requests

base_url = "https://reqres.in/api"
user_id = 0

@allure.feature('User Feature')
@allure.suite('Create User Suite')
@allure.title('Test Create User')
@allure.description('Test to create a user and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a user'):
        response = requests.post(
            f'{base_url}/users',
            json=data,
            headers=headers
        )

    with allure.step('Verify response status code is 201'):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify "id" is present in response'):
        assert "id" in response_data, "The response does not contain 'id'"

    with allure.step('Verify "name" is correct'):
        assert "name" in response_data, "The response does not contain 'name'"
        assert response_data['name'] == data['name'], f"Expected name to be {data['name']} but got '{response_data['name']}'"

    with allure.step('Verify "job" is correct'):
        assert "job" in response_data, "The response does not contain 'job'"
        assert response_data['job'] == data['job'], f"Expected job to be {data['job']} but got '{response_data['job']}'"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)

    global user_id
    user_id = response_data['id']