from flask import Flask
from controllers.auth import auth


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(auth)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
