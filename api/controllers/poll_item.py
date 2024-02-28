from prisma.models import PollItem      
from api.models.poll_dtos import PollItemDto
from flask import make_response, request, Blueprint, Response
from flask_restful import Resource, Api
from prisma.errors import UniqueViolationError
from werkzeug.exceptions import BadRequest

pollitem = Blueprint("pollitem", __name__, url_prefix="/pollitem")
pollitem_api = Api(pollitem)

# Creates a poll item
class PollItemCreate(Resource):
    def post(self):
        pollitem_dto = PollItemDto.from_json(request.json)
        try:
            PollItem.prisma().create(data=pollitem_dto.to_insertable())
            poll_item = PollItem.prisma().find_first(where={"pollId": pollitem_dto.pollId, "description": pollitem_dto.description})
        except UniqueViolationError:
            raise BadRequest("username not unique")
        return make_response({"description": poll_item.description, "votes": poll_item.votes, "id": poll_item.id})
    
class PollItemDetails(Resource):
    def get(self, poll_item_id):
        try:
            poll_item = PollItem.prisma().find_first(where={"id": poll_item_id})
        except UniqueViolationError:
            raise BadRequest
        return make_response({"description": poll_item.description, "votes": poll_item.votes})

pollitem_api.add_resource(PollItemCreate, "/create")
pollitem_api.add_resource(PollItemDetails, "/<poll_item_id:poll_item_id>")