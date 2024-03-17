"""Contains the BaseDTO class"""

from dataclasses import asdict
from werkzeug.exceptions import BadRequest
import jsonschema

# In order to keep JSON -> Python conversion easily readable,
# we use the original camelCase naming convention
# pylint: disable=invalid-name


class BaseDto:
    """All other DTOs inherit stuff from this one."""

    def to_insertable(self, include_null=False) -> dict:
        """Convert the DTO into a dict for use with Prisma"""
        exclude_fields = ["schema"]
        if include_null:
            return {k: v for k, v in asdict(self).items() if k not in exclude_fields}
        return {
            k: v
            for k, v in asdict(self).items()
            if v is not None and k not in exclude_fields
        }

    @staticmethod
    def validate(data: dict, schema: dict):
        """Validate the data properties
        data: request.json
        schema: JSON-schema dict

        raises BadRequest error if invalid
        """
        try:
            jsonschema.validate(
                instance=data,
                schema=schema,
                format_checker=jsonschema.FormatChecker(),
            )
        except jsonschema.exceptions.ValidationError as e:
            raise BadRequest(e.message)
        except jsonschema.exceptions.FormatError as e:
            raise BadRequest(e.message)
