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

poll_patch_spec = {
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "poll",
            "in": "path",
            "description": "The ID of the poll",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/poll-patch",
                }
            }
        },
    },
    "responses": {
        "200": {"description": "Return the requested poll"},
        "401": {"description": "Unauthorized request"},
    },
}

poll_item_patch_spec = {
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "poll_item",
            "in": "path",
            "description": "The ID of the poll item",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/poll-item-patch",
                }
            }
        },
    },
    "responses": {
        "200": {"description": "Return the requested poll item"},
        "401": {"description": "Unauthorized request"},
    },
}

poll_with_converter_specs = {
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "poll",
            "in": "path",
            "description": "The ID of the poll",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {"description": "Return the requested poll"},
        "204": {"description": "Success, but no content to return"},
        "403": {"description": "Unauthorized request"},
    },
}

poll_without_body_specs = {
    "security": [{"BearerAuth": []}],
    "responses": {
        "200": {"description": "Return all polls not marked private"},
        "401": {"description": "Unauthorized request"},
    },
}

pollitem_without_body_specs = {
    "security": [{"BearerAuth": []}],
    "responses": {
        "200": {"description": "Return all polls not marked private"},
        "401": {"description": "Unauthorized request"},
    },
}

pollitem_with_converter_specs = {
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "poll_item",
            "in": "path",
            "description": "The ID of the poll item",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {"description": "Return the requested poll item"},
        "204": {"description": "Success, but no content to return"},
        "401": {"description": "Unauthorized request"},
        "403": {"description": "Unauthorized request"},
    },
}

pollitem_with_converter_no_auth_specs = {
    "parameters": [
        {
            "name": "poll_item",
            "in": "path",
            "description": "The ID of the poll item",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "201": {"description": "Success, registered vote"},
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
