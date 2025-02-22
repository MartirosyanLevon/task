import pytest

from api.base_model.user_api import UserAPI
from api.utils.faker import generate_invalid_user_data  # ✅ Import fake data generator


@pytest.fixture
def user_api():
    """Provides a fresh UserAPI instance for each test."""
    return UserAPI()


### ❌ Negative Registration Test Cases

@pytest.mark.negative
@pytest.mark.parametrize("invalid_user", generate_invalid_user_data())  # ✅ Uses Faker-generated invalid data
def test_register_invalid_user(user_api, invalid_user):
    """Negative: Try to register a user with invalid data."""
    response = user_api.register_user(invalid_user["name"], invalid_user["email"], invalid_user["password"])
    assert response.status_code == 400, f"Expected 400 Bad Request, but got: {response.text}"
