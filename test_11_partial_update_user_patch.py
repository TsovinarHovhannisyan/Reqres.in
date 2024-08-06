import allure
import pytest
import requests
import test_6_creat_user_Post

base_url = "https://reqres.in/api"


@allure.feature('User Feature')
@allure.suite('Partial Update User Suite')
@allure.title('Test Partial Update User')
@allure.description('Test to partially update a user and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_partial_update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send PATCH request to partially update a user'):
        response = requests.patch(
            f'{base_url}/users/{test_6_creat_user_Post.user_id}',
            json=data,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify "job" is correct'):
        assert response_data['job'] == data['job'], f"Expected job to be {data['job']} but got '{response_data['job']}'"

    with allure.step('Verify "name" is correct'):
        assert response_data['name'] == data['name'], f"Expected name to be {data['name']} but got '{response_data['name']}'"

    with allure.step('Verify response contains "updatedAt"'):
        assert 'updatedAt' in response_data, "Response should contain 'updatedAt' field"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)