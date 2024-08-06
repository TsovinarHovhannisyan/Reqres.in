import allure
import pytest
import requests

base_url = "https://reqres.in/api"

@allure.feature('User Feature')
@allure.suite('Get Users Suite')
@allure.title('Test Get Users Page 2')
@allure.description('Test to retrieve the list of users from page 2 and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_users_page_2():
    with allure.step('Send GET request to retrieve users from page 2'):
        response = requests.get(f'{base_url}/users?page=2')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response structure'):
        assert response_data['page'] == 2, "Expected page to be 2"
        assert response_data['per_page'] == 6, "Expected per_page to be 6"
        assert response_data['total'] == 12, "Expected total to be 12"
        assert response_data['total_pages'] == 2, "Expected total_pages to be 2"

    with allure.step('Verify data field contains 6 users'):
        assert len(response_data['data']) == 6, "Expected 6 users in data field"

    with allure.step('Verify each user data'):
        users = response_data['data']
        for user in users:
            assert 'id' in user, "User ID is missing"
            assert 'email' in user, "User email is missing"
            assert 'first_name' in user, "User first name is missing"
            assert 'last_name' in user, "User last name is missing"
            assert 'avatar' in user, "User avatar is missing"

    with allure.step('Verify support fields'):
        assert 'support' in response_data, "The response does not contain 'support'"
        support_data = response_data['support']
        assert 'url' in support_data, "Support URL is missing"
        assert 'text' in support_data, "Support text is missing"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)