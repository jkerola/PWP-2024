"""Contains tests for authorization related routes"""

from secrets import token_hex
from prisma.models import User

credentials = {
    "username": "testuser",
    "password": token_hex(16),
}

headers = {"Content-Type": "application/json"}


def teardown():
    """Called after every test"""
    User.prisma().delete_many()


# Utility functions
def register(client, credentials=credentials):
    """Utility function for creating a user"""
    return client.post("/auth/register", json=credentials, headers=headers)


def login(client, credentials=credentials) -> str:
    """Utility function for logging in with user credentials"""
    return client.post("/auth/login", json=credentials, headers=headers)


# Tests start here
def test_user_can_register(client):
    """User is able to register with correct credentials"""
    response = register(client)
    assert response.status_code == 201
    user = User.prisma().find_unique({"username": credentials["username"]})
    assert user is not None
    assert user.username == credentials["username"]


def test_bad_credentials_raise_error(client):
    """Missing or improper fields should throw error"""
    response = client.post(
        "/auth/register", json={"username": "missing-password"}, headers=headers
    )
    assert response.status_code == 400


def test_user_can_login(client):
    """User can login with correct credentials"""
    register(client)
    response = login(client)
    assert response.status_code == 200
    assert "access_token" in response.json


def test_invalid_credentials_raise_error(client):
    """Invalid credentials should be met with appropriate error"""
    response = login(client, {"username": "invaliduser", "password": token_hex(16)})
    assert response.status_code == 401


def test_authenticated_routes_are_protected(client):
    """Authenticated routes are only accessible with bearer token"""
    response = client.get("/auth/profile", headers=headers)
    assert response.status_code == 401
    register(client)
    token = login(client).json["access_token"]
    response = client.get(
        "/auth/profile",
        headers={"Authorization": f"Bearer {token}", **headers},
    )
    assert response.status_code == 200
    assert response.json["username"] == credentials["username"]
