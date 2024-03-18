"""Contains route specification files"""

# TODO: fill in descriptions, other routes
register_specs = {
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/register",
                }
            }
        },
    },
}

login_specs = {
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/login",
                }
            }
        },
    },
    "responses": {
        "200": {
            "description": "OK",
        }
    }
}

poll_specs = {
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/poll",
                }
            }
        },
    }
}

profile_specs = {
    "security": ["Bearer"],
}

poll_item_specs = {
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/poll-item",
                }
            }
        },
    }
}
