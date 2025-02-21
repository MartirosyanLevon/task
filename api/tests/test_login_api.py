import pytest

from base_model.user_api import UserAPI
from utils.faker import generate_user_data, generate_invalid_login_data  # ✅ Import fake data generator


@pytest.fixture
def user_api():
    """Provides a fresh UserAPI instance for each test."""
    return UserAPI()


### ✅ Positive Login Test Cases

@pytest.mark.positive
def test_login_valid_user(user_api):
    """Positive: Login after registering a user."""
    user_data = generate_user_data()

    # Register user first
    user_api.register_user(user_data["name"], user_data["email"], user_data["password"])

    # Try logging in
    response = user_api.login(user_data["email"], user_data["password"])
    assert response.status_code == 200, "Login failed"


### ❌ Negative Login Test Cases

@pytest.mark.negative
@pytest.mark.parametrize("email, password, expected_status",
                         generate_invalid_login_data())  # ✅ Uses Faker-generated invalid logins
def test_login_invalid_user(user_api, email, password, expected_status):
    """Negative: Attempt to log in with invalid credentials."""
    response = user_api.login(email, password)
    assert response.status_code == expected_status, f"Expected {expected_status}, but got: {response.text}"
