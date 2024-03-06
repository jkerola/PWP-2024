"""Module for Poll related DTOs"""

from datetime import datetime
from dataclasses import dataclass, asdict
from api.models.base_dto import BaseDto

# In order to keep JSON -> Python conversion easily readable,'
# we use the original camelCase naming convention
# pylint: disable=invalid-name


@dataclass(frozen=True)
class PollItemDto(BaseDto):
    """DTO for managing pollItems"""

    pollId: str
    description: str

    @staticmethod
    def from_json(data: dict):
        """Create a new DTO from json
        data: request.json
        """
        PollItemDto.validate(
            data,
            {
                "type": "object",
                "properties": {
                    "pollId": {"type": "string"},
                    "description": {"type": "string"},
                },
                "required": ["pollId", "description"],
            },
        )

        return PollItemDto(
            pollId=data.get("pollId"),
            description=data.get("description"),
        )

    def to_json(self):
        """Return the object as JSON"""
        return asdict(self)


@dataclass(frozen=True)
class PollDto(BaseDto):
    """DTO for managing polls"""

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
            data,
            {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "expires": {"type": "string", "format": "date-time"},
                    "description": {"type": "string"},
                    "multipleAnswers": {"type": "boolean"},
                    "private": {"type": "boolean"},
                },
                "required": ["title", "expires"],
            },
        )

        return PollDto(
            description=data.get("description"),
            title=data.get("title"),
            expires=data.get("expires"),
            multipleAnswers=data.get("multipleAnswers"),
            private=data.get("private"),
        )
