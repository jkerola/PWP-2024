"""Contains pytest fixtures for setting up the test environment"""

import os
from secrets import token_hex
from dotenv import load_dotenv
from pytest import fixture
from api.app import create_app

load_dotenv()


@fixture(name="credentials", scope="session")
def get_credentials():
    """Creates random credentials for the session"""
    return {
        "username": "testuser",
        "password": token_hex(16),
    }


@fixture(name="db", autouse=True, scope="session")
def setup_db():
    """Fixture for setting up prisma models"""
    print("Remember to start the database before testing!")
    os.environ["DB_NAME"] = "test"
    p = os.popen("prisma generate && prisma db push")
    print(p.read())
    p.close()
    yield


@fixture(name="app")
def setup_app():
    """Fixture for setting up flask"""
    app = create_app()
    yield app


@fixture(name="runner")
def setup_runner(app):
    """Fixture for setting up the CLI runner"""
    return app.test_cli_runner()


@fixture(name="client")
def setup_client(app):
    """Fixture for setting up the test client"""
    return app.test_client()
