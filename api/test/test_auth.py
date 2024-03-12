"""Contains tests for authorization related routes"""

from secrets import token_hex
from prisma.models import User


# Tests start here
def test_user_can_register(client, credentials):
    """User is able to register with correct credentials"""
    response = client.post(
        "/auth/register",
        json=credentials,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 201
    user = User.prisma().find_unique({"username": credentials["username"]})
    assert user is not None
    assert user.username == credentials["username"]


def test_bad_credentials_raise_error(client):
    """Missing or improper fields should throw error"""
    response = client.post(
        "/auth/register",
        json={"username": "missing-password"},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 400


def test_user_can_login(client, credentials, user):
    """User can login with correct credentials"""
    response = client.post(
        "/auth/login",
        json=credentials,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json


def test_invalid_credentials_raise_error(client):
    """Invalid credentials should be met with appropriate error"""
    response = client.post(
        "/auth/login",
        json={"username": "invaliduser", "password": token_hex(16)},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 401


def test_authenticated_routes_are_protected(client, auth):
    """Authenticated routes are only accessible with bearer token"""
    headers = {"Content-Type": "application/json"}
    response = client.get("/auth/profile", headers=headers)
    assert response.status_code == 401
    response = client.get("/auth/profile", headers=auth)
    assert response.status_code == 200
