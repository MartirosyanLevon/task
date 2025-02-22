import uuid
from locust import HttpUser, task, between
from faker import Faker
from logger_config import logger  # ✅ Import logger from separate config file

fake = Faker()

class UserBehavior(HttpUser):
    wait_time = between(1, 3)  # Simulates real user wait time
    host = "https://cinema.xdatagroup.dev/api/v1/cinema"  # Set base URL

    @task
    def register_login_unregister(self):
        """Simulate user registration, login, and unregistration."""

        # ✅ Generate unique user data
        user_data = {
            "name": fake.name(),
            "email": f"user_{uuid.uuid4().hex[:6]}@test.com",  # Ensures unique email
            "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
        }

        # ✅ Register the user
        register_response = self.client.post("/user/register", json=user_data)

        if register_response.status_code in [200, 201]:  # Only proceed if registration succeeds
            logger.info(f"User {user_data['email']} registered successfully.")

            # ✅ Try logging in
            login_data = {
                "email": user_data["email"],
                "password": user_data["password"],
            }
            login_response = self.client.post("/user/login", json=login_data)

            if login_response.status_code == 200:
                logger.info(f"User {user_data['email']} logged in successfully.")

                # ✅ Extract the access token
                access_token = login_response.json().get("accessToken", {}).get("value")
                if access_token:
                    # ✅ Unregister the user
                    headers = {"Authorization": f"Bearer {access_token}"}
                    unregister_response = self.client.post("/user/unregister", headers=headers)

                    if unregister_response.status_code in [200, 204]:
                        logger.info(f"User {user_data['email']} unregistered successfully.")
                    else:
                        logger.error(f"Failed to unregister user {user_data['email']}: {unregister_response.text}")
                else:
                    logger.warning(f"Access token missing for user {user_data['email']}")
            else:
                logger.error(f"Login failed for user {user_data['email']}: {login_response.text}")
        else:
            logger.error(f"Registration failed for user {user_data['email']}: {register_response.text}")

    def on_start(self):
        """Executed when a simulated user starts running."""
        logger.info("Starting Locust performance test for /user/register, /user/login, and /user/unregister")
