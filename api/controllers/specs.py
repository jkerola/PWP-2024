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
}

profile_specs = {
    "security": ["Bearer"],
}
