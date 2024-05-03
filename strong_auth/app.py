from flask import Flask
from flask_cors import CORS
import waitress
from auth import auth_controller


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    return app


app = create_app()
CORS(app)

if __name__ == "__main__":
    waitress.serve(app.wsgi_app, port=5001, url_scheme="http")
