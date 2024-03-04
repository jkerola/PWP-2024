from prisma.models import PollItem
from api.models.poll_dtos import PollItemDto
from flask import make_response, request, Blueprint
from flask_restful import Resource, Api
from prisma.errors import UniqueViolationError
from werkzeug.exceptions import BadRequest

pollitem = Blueprint("pollitem", __name__, url_prefix="/pollitems")
pollitem_api = Api(pollitem)


class PollItemCreate(Resource):
    """
    Creates a PollItem.

    Send a POST request to /pollitems with:
    "pollId": Poll ID to append this PollItem to.
    "description": Description of the PollItem.

    returns:

    {

    "description": Description of the created PollItem.
    "votes": Vote count of the created PollItem.
    "id": ID of the created PollItem.

    }
    """

    def post(self):
        pollitem_dto = PollItemDto.from_json(request.json)
        try:
            PollItem.prisma().create(data=pollitem_dto.to_insertable())
            poll_item = PollItem.prisma().find_first(
                where={
                    "pollId": pollitem_dto.pollId,
                    "description": pollitem_dto.description,
                }
            )
        except UniqueViolationError:
            raise BadRequest("username not unique")
        return make_response(
            {
                "description": poll_item.description,
                "votes": poll_item.votes,
                "id": poll_item.id,
            }
        )


class PollItemDetails(Resource):
    """
    Gets a single PollItem based on id.

    Send a GET request to /pollitems/<poll_item_id:poll_item_id> with:
    "id": id of the PollItem.

    returns {

    "desctipition": Description of the retrieved PollItem.
    "votes": Amount of votes the PollItem has.

    }
    """

    def get(self, poll_item_id):
        try:
            poll_item = PollItem.prisma().find_first(where={"id": poll_item_id})
        except UniqueViolationError:
            raise BadRequest
        return make_response(
            {"description": poll_item.description, "votes": poll_item.votes}
        )


class PollItemDelete(Resource):
    """
    Deletes a PollItem with given id.

    Send a DELETE request to /pollitems/<poll_item_id:poll_item_id> with:

    "id": id of the PollItem to delete.

    returns {

    "deleted item": id of the deleted PollItem.

    }

    """

    def delete(self, poll_item_id):
        try:
            PollItem.prisma().delete(where={"id": poll_item_id})
        except UniqueViolationError:
            raise BadRequest
        return make_response({"deleted item": poll_item_id})


class PollItemUpdate(Resource):
    """
    Updates a PollItem with given id.

    Sends a PATCH request to /pollitems/<poll_item_id:poll_item_id> with:

    "id": id of the PollItem to patch.

    returns {

    "description": description of the updated PollItem.
    "votes": amount of votes the updated PollItem has.

    }

    """

    def patch(self, poll_item_id):
        pollitem_dto = PollItemDto.from_json(request.json)
        try:
            PollItem.prisma().update(
                where={"id": poll_item_id}, data=pollitem_dto.to_insertable()
            )
            poll_item = PollItem.prisma().find_first(where={"id": poll_item_id})
        except UniqueViolationError:
            raise BadRequest
        return make_response(
            {"description": poll_item.description, "votes": poll_item.votes}
        )


pollitem_api.add_resource(PollItemCreate, "")
pollitem_api.add_resource(PollItemDetails, "/<poll_item_id:poll_item_id>")
pollitem_api.add_resource(PollItemDelete, "/<poll_item_id:poll_item_id>")
pollitem_api.add_resource(PollItemUpdate, "/<poll_item_id:poll_item_id>")
