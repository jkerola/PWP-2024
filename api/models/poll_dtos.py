"""Module for Poll related DTOs"""

from datetime import datetime
from dataclasses import dataclass
from werkzeug.exceptions import BadRequest
from api.models.base_dto import BaseDto
from dateutil import parser

# In order to keep JSON -> Python conversion easily readable,'
# we use the original camelCase naming convention
# pylint: disable=invalid-name


@dataclass(frozen=True)
class PollItemDto(BaseDto):
    """DTO for managing pollItems"""

    pollId: str
    description: str
    votes: int = 0

    @staticmethod
    def from_json(data: dict):
        """Create a new DTO from json
        data: request.json
        """
        PollItemDto.validate([("pollId", str)], data)

        return PollItemDto(
            pollId=data.get("pollId"),
            description=data.get("description"),
            votes=0,
        )


@dataclass(frozen=True)
class PollDto(BaseDto):
    """DTO for managing polls"""

    userId: str
    title: str
    description: str
    expires: datetime
    private: bool = False
    multipleAnswers: bool = False

    @staticmethod
    def from_json(data: dict):
        """Create a new DTO from json
        data: request.json
        """
        PollDto.validate(
            [
                ("userId", str),
                ("title", str),
                ("expires", str),
            ],
            data,
        )

        date = data.get("expires")
        if date is None:
            raise BadRequest("property 'expires' is required")
        try:
            date = parser.parse(date)
        except parser.ParserError:
            raise BadRequest("property 'expires' should be ISO format date")

        return PollDto(
            userId=data.get("userId"),
            description=data.get("description"),
            title=data.get("title"),
            expires=date,
            multipleAnswers=data.get("multipleAnswers"),
            private=data.get("private"),
        )
