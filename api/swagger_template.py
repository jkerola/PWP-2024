"""Contains the Swagger default configuration"""

from api.models import schemas

template = {
    "components": {
        "schemas": {
            "register": schemas.register_schema,
            "login": schemas.login_schema,
            "poll": schemas.poll_schema,
            "poll-item": schemas.poll_item_schema,
        },
        "examples": {},
        "securitySchemes": {
            "Bearer": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        },
    },
}
