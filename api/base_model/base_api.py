import requests

from config import BASE_URL  # Import the centralized BASE_URL


class BaseAPI:
    """Base class for API requests, handling authentication and common operations."""

    def __init__(self):
        """Initialize a session for API requests."""
        self.session = requests.Session()
        self.base_url = BASE_URL
        self.access_token = None
        self.refresh_token = None

    def get(self, endpoint, params=None):
        """Send a GET request."""
        return self.session.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint, data=None):
        """Send a POST request."""
        return self.session.post(f"{self.base_url}{endpoint}", json=data)

    def put(self, endpoint, data=None):
        """Send a PUT request."""
        return self.session.put(f"{self.base_url}{endpoint}", json=data)

    def delete(self, endpoint):
        """Send a DELETE request."""
        return self.session.delete(f"{self.base_url}{endpoint}")
