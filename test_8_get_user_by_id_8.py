import allure
import pytest
import requests


base_url = "https://reqres.in/api"

@allure.feature('User Feature')
@allure.suite('Get User by ID Suite')
@allure.title('Test Get User by ID 2')
@allure.description('Test to retrieve a user by ID and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_user_by_id():
    user_id = 2
    with allure.step(f'Send GET request to retrieve user with ID {user_id}'):
        response = requests.get(f'{base_url}/users/{user_id}')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response structure'):
        assert 'data' in response_data, "Response should contain 'data' field"
        assert 'support' in response_data, "Response should contain 'support' field"

    with allure.step('Verify data fields'):
        user_data = response_data['data']
        assert user_data['id'] == user_id, f"Expected user ID to be {user_id}, but got {user_data['id']}"
        assert user_data['email'] == "janet.weaver@reqres.in", "Unexpected user email"
        assert user_data['first_name'] == "Janet", "Unexpected user first name"
        assert user_data['last_name'] == "Weaver", "Unexpected user last name"
        assert user_data['avatar'] == "https://reqres.in/img/faces/2-image.jpg", "Unexpected user avatar"

    with allure.step('Verify support fields'):
        support_data = response_data['support']
        assert support_data['url'] == "https://reqres.in/#support-heading", "Unexpected support URL"
        assert support_data['text'] == "To keep ReqRes free, contributions towards server costs are appreciated!", "Unexpected support text"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)