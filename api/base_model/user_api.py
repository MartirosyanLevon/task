from base_model.base_api import BaseAPI


class UserAPI(BaseAPI):
    """Handles User-related API actions like registration, login, and profile management."""

    def register_user(self, name, email, password):
        """Register a new user."""
        payload = {"name": name, "email": email, "password": password}
        return self.post("/user/register", payload)

    def login(self, email, password):
        """Login user and store token."""
        payload = {"email": email, "password": password}
        response = self.post("/user/login", payload)

        if response.status_code == 200:
            self.token = response.json().get("token")
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})

        return response


