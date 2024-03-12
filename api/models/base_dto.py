"""Contains the BaseDTO class"""

from dataclasses import asdict
from werkzeug.exceptions import BadRequest
from jsonschema import validate, FormatChecker
from jsonschema.exceptions import ValidationError, FormatError

# In order to keep JSON -> Python conversion easily readable,
# we use the original camelCase naming convention
# pylint: disable=invalid-name


class BaseDto:
    """All other DTOs inherit stuff from this one."""

    def to_insertable(self, include_null=False) -> dict:
        """Convert the DTO into a dict for use with Prisma"""
        if include_null:
            return asdict(self)
        return {k: v for k, v in asdict(self).items() if v is not None}

    @staticmethod
    def validate(data: dict, schema: dict):
        """Validate the data properties
        data: request.json
        props: ex: [('username', str)]

        raises BadRequest error if invalid
        """
        try:
            validate(
                instance=data,
                schema=schema,
                format_checker=FormatChecker(),
            )
        except ValidationError as e:
            raise BadRequest(e.message)
        except FormatError as e:
            raise BadRequest(e.message)
