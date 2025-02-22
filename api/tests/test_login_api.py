import pytest

from api.base_model.user_api import UserAPI
from api.utils.faker import generate_user_data, generate_invalid_login_data  # ✅ Import fake data generator


@pytest.fixture
def user_api():
    """Provides a fresh UserAPI instance for each test."""
    api = UserAPI()

    yield api  # Test execution happens here

    # ✅ Cleanup: Unregister only if a token exists (i.e., login was successful)
    if hasattr(api, "token"):
        response = api.unregister_user()
        assert response.status_code in [200, 204], f"Failed to unregister user: {response.text}"


### ✅ Positive Login Test Cases

@pytest.mark.positive
def test_login_valid_user(user_api):
    """Positive: Login after registering a user."""
    user_data = generate_user_data()

    # ✅ Register user first
    register_response = user_api.register_user(user_data["name"], user_data["email"], user_data["password"])
    # ✅ Validate response status code
    assert register_response.status_code in [200, 201], f"Registration failed: {register_response.text}"
    # ✅ Assert the response message
    assert register_response.json()["message"] == "User registered", f"Unexpected message: {register_response.json()}"
    assert "userId" in register_response.json(), "userId is missing in the response!"

    # ✅ Try logging in
    login_response = user_api.login(user_data["email"], user_data["password"])
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"


### ❌ Negative Login Test Cases

@pytest.mark.negative
@pytest.mark.parametrize("email, password, expected_status",
                         generate_invalid_login_data())  # ✅ Uses Faker-generated invalid logins
def test_login_invalid_user(user_api, email, password, expected_status):
    """Negative: Attempt to log in with invalid credentials."""
    response = user_api.login(email, password)
    assert response.status_code == expected_status, f"Expected {expected_status}, but got: {response.text}"
