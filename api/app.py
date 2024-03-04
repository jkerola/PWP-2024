"""Module for configuring the Flask application"""

from flask import Flask
from werkzeug.exceptions import HTTPException
from api.controllers.auth import auth
from api.controllers.polls import polls
from api.controllers.poll_items import poll_items
from api.database import connect_to_db
from api.middleware.error_handler import handle_exception
from api.converters.poll import PollConverter
from api.converters.poll_item import PollItemConverter


def create_app() -> Flask:
    """Factory function"""
    app = Flask(__name__)
    app.url_map.converters["poll_id"] = PollConverter
    app.url_map.converters["poll_item_id"] = PollItemConverter
    app.register_blueprint(auth)
    app.register_blueprint(polls)
    app.register_blueprint(poll_items)
    app.register_error_handler(HTTPException, handle_exception)
    return app


connect_to_db()
application = create_app()
