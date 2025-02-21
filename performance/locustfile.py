import uuid
from locust import HttpUser, task, between
from faker import Faker

fake = Faker()

class UserBehavior(HttpUser):
    wait_time = between(1, 3)  # Simulates real user wait time

    @task
    def register_and_login(self):
        """Simulate user registration and login."""

        # Generate unique user data
        user_data = {
            "name": fake.name(),
            "email": f"user_{uuid.uuid4().hex[:6]}@test.com",  # Ensures unique email
            "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
        }

        # Register the user
        register_response = self.client.post("/user/register", json=user_data)

        if register_response.status_code == 201:  # Only proceed if registration succeeds
            # Try logging in with the registered user
            login_data = {
                "email": user_data["email"],
                "password": user_data["password"],
            }
            login_response = self.client.post("/user/login", json=login_data)

            # Optionally, check if login was successful
            if login_response.status_code != 200:
                print(f"Login failed for user {user_data['email']}")

    def on_start(self):
        """Executed when a simulated user starts running."""
        print("Starting Locust performance test for /user/register and /user/login")

    # Set base URL
    host = "https://cinema.xdatagroup.dev/api/v1/cinema"
