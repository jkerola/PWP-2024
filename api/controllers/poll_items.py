"""Module containing PollItem routes"""

from flask import make_response, request, Blueprint
from flask_restful import Resource, Api
from werkzeug.exceptions import Forbidden, NotFound
from prisma.models import PollItem, Poll, User
from api.models.poll_dtos import PollItemDto
from api.middleware.authguard import requires_authentication

poll_items_bp = Blueprint("pollitems", __name__, url_prefix="/pollitems")
poll_items_api = Api(poll_items_bp)


class PollItemCollection(Resource):
    """Route resource representing all user-created PollItems"""

    method_decorators = [requires_authentication]

    def get(self, user: User):
        """Returns a list of PollItems associated with the resource"""
        polls = (
            User.prisma()
            .find_unique(
                where={"id": user.id},
                include={"polls": True},
            )
            .polls
        )
        poll_items = PollItem.prisma().find_many(
            where={
                "pollId": {"in": [poll.id for poll in polls]},
            },
        )
        data = [item.model_dump(exclude="poll") for item in poll_items]

        return make_response(data)

    def post(self, user: User):
        """Creates a PollItem.

        Send a POST request to /pollitems with:

        "pollId": Poll ID to append this PollItem to.
        "description": Description of the PollItem.

        returns:

        {

            "description": Description of the created PollItem.
            "votes": Vote count of the created PollItem.
            "id": ID of the created PollItem.

        }"""
        pollitem_dto = PollItemDto.from_json(request.json)
        poll = Poll.prisma().find_unique(
            where={
                "userId": user.id,
                "id": pollitem_dto.pollId,
            }
        )
        if poll is None:
            raise NotFound("user has no polls matching given id")
        poll_item = PollItem.prisma().create(data=pollitem_dto.to_insertable())
        return make_response(poll_item.model_dump(exclude=["poll"]))


class PollItemResource(Resource):
    """Route resource representing a single Pollitem"""

    method_decorators = {
        "patch": [requires_authentication],
        "delete": [requires_authentication],
    }

    def get(self, poll_item: PollItem):
        """Gets a single PollItem based on id.

        Send a GET request to /pollitems/<poll_item_id:poll_item_id> with:
        "id": id of the PollItem.

        returns {

            "desctipition": Description of the retrieved PollItem.
            "votes": Amount of votes the PollItem has.

        }"""

        return make_response(poll_item.model_dump(exclude="poll"))

    def post(self, poll_item: PollItem):
        """Vote on a post!"""
        PollItem.prisma().update(
            where={"id": poll_item.id},
            data={"votes": poll_item.votes + 1},
        )
        return make_response("", 201)

    def patch(self, poll_item: PollItem, user: User):
        """Updates a PollItem with given id.

        Sends a PATCH request to /pollitems/<id> with:

        "id": id of the PollItem to patch.

        returns
        {
            "description": description of the updated PollItem.
            "votes": amount of votes the updated PollItem has.
        }"""
        pollitem_dto = PollItemDto.from_json(request.json)
        poll = Poll.prisma().find_unique(where={"id": poll_item.pollId})
        if poll.userId != user.id:
            raise Forbidden()

        updated = PollItem.prisma().update(
            where={"id": poll_item.id},
            data=pollitem_dto.to_insertable(),
        )
        return make_response(updated.model_dump(exclude="poll"))

    def delete(self, poll_item: PollItem, user: User):
        """Deletes a PollItem with given id.

        Send a DELETE request to /pollitems/<poll_item_id:poll_item_id> with:

        "id": id of the PollItem to delete.

        returns {

            "deleted item": id of the deleted PollItem.

        }"""

        poll = Poll.prisma().find_unique(where={"id": poll_item.pollId})
        if poll.userId != user.id:
            raise Forbidden()
        PollItem.prisma().delete(where={"id": poll_item.id})
        return make_response()


poll_items_api.add_resource(PollItemCollection, "")
poll_items_api.add_resource(PollItemResource, "/<poll_item:poll_item>")
