from api.base_model.base_api import BaseAPI


class UserAPI(BaseAPI):
    """Handles User-related API actions like registration, login, and profile management."""

    def register_user(self, name, email, password):
        """Register a new user."""
        payload = {"name": name, "email": email, "password": password}
        return self.post("/user/register", payload)

    def login(self, email, password):
        """Login user and store accessToken."""
        payload = {"email": email, "password": password}
        response = self.post("/user/login", payload)

        if response.status_code == 200:
            response_data = response.json()
            self.token = response_data["accessToken"]["value"]  # ✅ Extract token
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})  # ✅ Store in session

        return response

    def unregister_user(self):
        """Unregister the user using the stored accessToken."""
        if not hasattr(self, "token"):
            raise ValueError("Cannot unregister: No access token found. Ensure login was successful.")

        url = f"{self.base_url}/user/unregister"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = self.session.post(url, headers=headers)
        return response


