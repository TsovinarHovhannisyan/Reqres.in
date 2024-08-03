import allure
import pytest
import requests

base_url = "https://reqres.in/api"

@allure.feature('User Feature')
@allure.suite('Get Users with Delay Suite')
@allure.title('Test Get Users with Delay')
@allure.description('Test to get users with a delay and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_get_users_with_delay():
    params = {'delay': 3}
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send GET request to fetch users with delay'):
        response = requests.get(
            f'{base_url}/users',
            params=params,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains expected keys'):
        assert "page" in response_data, "The response does not contain 'page'"
        assert "per_page" in response_data, "The response does not contain 'per_page'"
        assert "total" in response_data, "The response does not contain 'total'"
        assert "total_pages" in response_data, "The response does not contain 'total_pages'"
        assert "data" in response_data, "The response does not contain 'data'"
        assert "support" in response_data, "The response does not contain 'support'"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)