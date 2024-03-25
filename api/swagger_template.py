"""Contains the Swagger default configuration"""

from api.models import schemas

template = {
    "components": {
        "schemas": {
            "register": schemas.register_schema,
            "login": schemas.login_schema,
            "poll": schemas.poll_schema,
            "poll-item": schemas.poll_item_schema,
            "poll-patch": schemas.poll_patch_schema,
            "poll-item-patch": schemas.poll_item_patch_schema,
        },
        "examples": {},
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        },
    },
}
