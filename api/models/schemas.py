"""Contains JSON-Schema dicts for validation and documentation"""

register_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string", "description": "Must be unique"},
        "password": {"type": "string"},
        "email": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
    },
    "required": ["username", "password"],
}


login_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["username", "password"],
}


partial_poll_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "expires": {"type": "string", "format": "date-time"},
        "description": {"type": "string"},
        "multipleAnswers": {"type": "boolean"},
        "private": {"type": "boolean"},
    },
}

poll_schema = {
    **partial_poll_schema,
    "required": ["title", "expires"],
}

poll_item_schema = {
    "type": "object",
    "properties": {
        "pollId": {"type": "string"},
        "description": {"type": "string"},
    },
    "required": ["pollId", "description"],
}
