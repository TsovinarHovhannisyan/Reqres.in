import allure
import pytest
import requests
import test_6_creat_user_Post

base_url = "https://reqres.in/api"

@allure.feature('User Feature')
@allure.suite('Get User by ID Suite')
@allure.title('Test Get User by ID 23')
@allure.description('Test to retrieve a user by an ID that does not exist and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_user_by_id():

    with allure.step(f'Send GET request to retrieve user with ID {test_6_creat_user_Post.user_id}'):
        response = requests.get(f'{base_url}/users/{test_6_creat_user_Post.user_id}')

    with allure.step('Verify response status code is 404'):
        assert response.status_code == 404, f'Expected Status Code 404, but got {response.status_code}'

    with allure.step('Verify response body is empty'):
        assert response.json() == {}, "Expected response body to be empty"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)