from flask import Flask
from api.controllers.auth import auth
from api.database import connect_to_db
from api.middleware.error_handler import handle_exception
from werkzeug.exceptions import HTTPException


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth)
    app.register_error_handler(HTTPException, handle_exception)
    return app


connect_to_db()
app = create_app()
