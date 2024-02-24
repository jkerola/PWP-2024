from prisma.models import Poll
from api.models.poll_dtos import PollDto
from flask import make_response, request, Blueprint, Response
from prisma.errors import UniqueViolationError
from werkzeug.exceptions import BadRequest

poll = Blueprint("poll", __name__)


@poll.route("/poll/create", methods=["POST"])
def create():
    poll_dto = PollDto.from_json(request.json)
    try:
        Poll.prisma().create(data=poll_dto.to_insertable())
        #finding the created poll
        poll = Poll.prisma().find_first(where={"title": poll_dto.title})
    except UniqueViolationError:
        raise BadRequest("username not unique")
    return make_response({"poll_id": poll.id})

@poll.route("/poll/pollitems", methods=["GET"])
def get_poll_items():
    poll_dto = PollDto.from_json(request.json)
    try:
        #find poll with pollid
        poll = Poll.prisma().find_first(where={"id": poll_dto.id})
    except UniqueViolationError:
        raise BadRequest("username not unique")
    return make_response({poll.items})