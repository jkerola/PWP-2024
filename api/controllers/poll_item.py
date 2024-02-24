from prisma.models import PollItem      
from api.models.poll_dtos import PollItemDto
from flask import make_response, request, Blueprint, Response
from prisma.errors import UniqueViolationError
from werkzeug.exceptions import BadRequest

pollitem = Blueprint("pollitem", __name__)

#Creates a pollitem
@pollitem.route("/pollitem/create", methods=["POST"])
def create_pollitem():
    pollitem_dto = PollItemDto.from_json(request.json)
    try:
        PollItem.prisma().create(data=pollitem_dto.to_insertable())
    except UniqueViolationError:
        raise BadRequest("username not unique")
    return make_response({"description": pollitem_dto.description, "votes": pollitem_dto.votes})