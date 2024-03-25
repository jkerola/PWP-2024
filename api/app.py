"""Module for configuring the Flask application"""

from flask import Flask
from werkzeug.exceptions import HTTPException
from flasgger import Swagger
from api.controllers.auth import auth_bp
from api.controllers.polls import polls_bp
from api.controllers.poll_items import poll_items_bp
from api.database import connect_to_db
from api.middleware.error_handler import handle_exception
from api.converters.poll import PollConverter
from api.converters.poll_item import PollItemConverter
from api.swagger_template import template


def create_app() -> Flask:
    """Factory function"""
    app = Flask(__name__)
    app.url_map.converters["poll"] = PollConverter
    app.url_map.converters["poll_item"] = PollItemConverter
    app.register_blueprint(auth_bp)
    app.register_blueprint(polls_bp)
    app.register_blueprint(poll_items_bp)
    app.register_error_handler(HTTPException, handle_exception)
    app.config["SWAGGER"] = {
        "title": "poll-api",
        "uiversion": 3,
        "openapi": "3.0.3",
    }
    return app


connect_to_db()
application = create_app()
swagger = Swagger(application, template=template)
