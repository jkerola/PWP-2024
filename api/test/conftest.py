"""Contains pytest fixtures for setting up the test environment"""

import os
import asyncio
import pytest_asyncio
import pytest
from datetime import datetime
from zoneinfo import ZoneInfo
from secrets import token_hex
from dotenv import load_dotenv
from api.app import create_app
from prisma.models import User, Poll, PollItem

load_dotenv()


@pytest.fixture(name="teardown", autouse=True, scope="function")
def teardown():
    """Called after every test"""
    User.prisma().delete_many()


@pytest.fixture(name="credentials", scope="session")
def get_credentials():
    """Creates random credentials for the session"""
    return {
        "username": "testuser",
        "password": token_hex(16),
    }


@pytest.fixture(name="poll_data")
def get_poll_data():
    return {
        "title": token_hex(16),
        "description": token_hex(16),
        "expires": datetime.now(tz=ZoneInfo("Europe/Helsinki")).isoformat(),
        "private": False,
    }


@pytest.fixture(name="poll_item_data")
def get_poll_item_data(poll) -> dict:
    return {"pollId": poll.id, "description": token_hex(16)}


@pytest.fixture(name="poll_item")
def insert_poll_item(poll_item_data, poll) -> PollItem:
    poll_item = PollItem.prisma().create(poll_item_data)
    return poll_item


@pytest.fixture(name="user")
def register_user(credentials, client) -> User:
    client.post(
        "/auth/register", json=credentials, headers={"Content-Type": "application/json"}
    )
    user = User.prisma().find_unique(where={"username": credentials["username"]})
    return user


@pytest.fixture(name="auth")
def login_user(credentials, client, user) -> dict:
    response = client.post(
        "/auth/login", json=credentials, headers={"Content-Type": "application/json"}
    )
    token = response.json["access_token"]
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }


@pytest.fixture(name="poll")
def insert_poll(poll_data, user) -> Poll:
    poll = Poll.prisma().create({**poll_data, "userId": user.id})
    return poll


@pytest_asyncio.fixture(name="db", autouse=True, scope="session")
async def setup_db():
    """Fixture for setting up prisma models"""
    print("Remember to start the database before testing!")

    os.environ["DB_NAME"] = "test"
    proc = await asyncio.create_subprocess_shell(
        "prisma generate && prisma db push",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    print(bytes.decode(stdout), flush=True)
    print(bytes.decode(stderr), flush=True)
    yield


@pytest.fixture(name="app")
def setup_app():
    """Fixture for setting up flask"""
    app = create_app()
    yield app


@pytest.fixture(name="runner")
def setup_runner(app):
    """Fixture for setting up the CLI runner"""
    return app.test_cli_runner()


@pytest.fixture(name="client")
def setup_client(app):
    """Fixture for setting up the test client"""
    return app.test_client()
