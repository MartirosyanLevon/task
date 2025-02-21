from faker import Faker

faker = Faker()


def generate_user_data():
    """Generate valid user registration data."""
    return {
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    }


def generate_invalid_user_data():
    """Generate different types of invalid user data with more realistic invalid emails."""
    invalid_emails = [
        faker.user_name(),  # Missing @domain
        f"{faker.user_name()}@{faker.word()}",  # Missing TLD
        f"{faker.user_name()}@.com",  # Invalid domain
        f"{faker.user_name()}@com",  # Missing dot before TLD
        f"{faker.user_name()}@example..com",  # Double dots in domain
        f"{faker.user_name()}@-example.com",  # Domain starts with a hyphen
        f"@{faker.domain_name()}",  # Missing username
        f"{faker.user_name()}@{faker.domain_name()} ",  # Trailing space
        f"{faker.user_name()}@{faker.domain_name()}!",  # Special character at the end
    ]

    return [
        {"name": "", "email": faker.email(), "password": faker.password()},  # Empty name
        {"name": faker.name(), "email": faker.random_element(invalid_emails), "password": faker.password()},
        # Faker-generated invalid email
        {"name": faker.name(), "email": faker.email(), "password": "123"},  # Weak password
        {"name": faker.name(), "email": faker.email(), "password": ""},  # Empty password
    ]


def generate_invalid_login_data():
    """Generate diverse invalid login credentials."""

    return [
        (faker.email(), faker.password(), 401),  # Random wrong credentials
        ("", "SomePass123", 400),  # Empty email
        (faker.email(), "", 400),  # Empty password
        ("", "", 400),  # Both email and password empty
        ("s", "", 400),  # Single-character email (invalid format, should fail validation)
    ]
