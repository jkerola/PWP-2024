from flask import Flask
from api.controllers.auth import auth
from api.controllers.poll import poll
from api.controllers.poll_item import pollitem
from api.database import connect_to_db
from api.middleware.error_handler import handle_exception
from werkzeug.exceptions import HTTPException
from api.converters.poll import PollConverter
from api.converters.poll_item import PollItemConverter


def create_app() -> Flask:
    app = Flask(__name__)
    app.url_map.converters["poll_id"] = PollConverter
    app.url_map.converters["poll_item_id"] = PollItemConverter
    app.register_blueprint(auth)
    app.register_blueprint(poll)
    app.register_blueprint(pollitem)
    app.register_error_handler(HTTPException, handle_exception)
    return app


connect_to_db()
app = create_app()
