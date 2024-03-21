"""Contains route specification files"""

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
    "responses": {
        "201": {"description": "User registered succesfully"},
        "400": {"description": "Request body contains errors"},
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
            "description": "Authentication succesful",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "access_token": {
                                "type": "string",
                                "description": "Bearer-type JWT access token",
                            },
                        },
                    }
                }
            },
        },
        "401": {"description": "Authorization rejected"},
    },
}

poll_specs = {
    "security": [{"BearerAuth": []}],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/poll",
                }
            }
        },
    },
    "responses": {
        "201": {
            "description": "Poll created succesfully",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/poll",
                    },
                }
            },
        },
        "401": {"description": "Unauthorized request"},
        "400": {"description": "Request body contains errors"},
    },
}

profile_specs = {
    "security": [{"BearerAuth": []}],
    "responses": {
        "200": {"description": "Display user information based on JWT contents"},
        "401": {"description": "Unauthorized request"},
    },
}

poll_item_specs = {
    "security": [{"BearerAuth": []}],
    "summary": "Create a PollItem",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/poll-item",
                }
            }
        },
    },
    "responses": {
        "201": {
            "description": "PollItem created succesfully",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/poll-item",
                    },
                }
            },
        },
        "401": {"description": "Unauthorized request"},
        "400": {"description": "Request body contains errors"},
    },
}
