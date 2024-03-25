"""Module for Poll related DTOs"""

from datetime import datetime
from dataclasses import dataclass
from api.models.base_dto import BaseDto
from api.models import schemas

# In order to keep JSON -> Python conversion easily readable,
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
        PollItemDto.validate(data, schemas.poll_item_schema)

        return PollItemDto(
            pollId=data.get("pollId"),
            description=data.get("description"),
        )


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
        PollDto.validate(data, schemas.poll_schema)

        return PollDto(
            description=data.get("description"),
            title=data.get("title"),
            expires=data.get("expires"),
            multipleAnswers=data.get("multipleAnswers"),
            private=data.get("private"),
        )


@dataclass(frozen=True)
class PartialPollDto(PollDto):
    """PollDto for patch requests, where not all fields are required"""

    @staticmethod
    def from_json(data: dict):
        """Create a new DTO from json
        data: request.json
        """
        PollDto.validate(data, schemas.partial_poll_schema)

        return PollDto(
            description=data.get("description"),
            title=data.get("title"),
            expires=data.get("expires"),
            multipleAnswers=data.get("multipleAnswers"),
            private=data.get("private"),
        )
