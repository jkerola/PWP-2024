from prisma.models import Poll
from api.models.poll_dtos import PollDto
from flask import request, Blueprint, Response
from prisma.errors import UniqueViolationError
from werkzeug.exceptions import BadRequest

poll = Blueprint("poll", __name__)


@poll.route("/poll/create", methods=["POST"])
def create():
    poll_dto = PollDto.from_json(request.json)
    try:
        Poll.prisma().create(data=poll_dto.to_insertable())
    except UniqueViolationError:
        raise BadRequest("username not unique")
    return Response(status=201)
