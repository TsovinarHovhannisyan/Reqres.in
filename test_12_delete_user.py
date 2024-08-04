import allure
import pytest
import requests
import test_6_creat_user_Post

base_url = "https://reqres.in/api"


@allure.feature('User Feature')
@allure.suite('Delete User Suite')
@allure.title('Test Delete User')
@allure.description('Test to delete a user and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user():
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send DELETE request to delete a user'):
        response = requests.delete(
            f'{base_url}/users/{test_6_creat_user_Post.user_id}',
            headers=headers
        )

    with allure.step('Verify response status code is 204'):
        assert response.status_code == 204, f'Expected Status Code 204, but got {response.status_code}'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)