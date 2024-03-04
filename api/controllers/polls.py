"""Module containing Poll routes"""

from flask import make_response, request, Blueprint
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest
from prisma.models import Poll, PollItem, User
from api.models.poll_dtos import PollDto
from api.middleware.authguard import requires_authentication

polls_bp = Blueprint("polls", __name__, url_prefix="/polls")
polls_api = Api(polls_bp)


class UniquePollItems(Resource):
    """Route resource representing PollItems related to a Poll"""

    def get(self, poll: Poll):
        """Gets all PollItems within a specified Poll.

        Send a GET request to /polls/<poll_id:poll_id>/pollitems with:

        "poll_id": Poll ID to query.

        returns:

        {

            "pollItems": list of PollItems.

        }"""
        poll_items = PollItem.prisma().find_many(where={"pollId": poll.id})
        data = [item.model_dump(exclude=["poll"]) for item in poll_items]
        return make_response(data)


class PollResource(Resource):
    """Route resource representing a polll"""

    method_decorators = {"post": [requires_authentication]}

    def get(self):
        """Returns all polls not marked private"""
        polls = Poll.prisma().find_many(where={"private": False})
        data = [poll.model_dump(exclude=["userId", "user", "items"]) for poll in polls]
        return make_response(data)

    def post(self, user: User):
        """Creates a Poll.

        Send a POST request to /polls with:
        {

            "title": title of the Poll.
            "description": description of the Poll.
            "expires": expiry date of Poll.
            "multipleAnswers": whether multiple answers should be allowed or not.
            "private": whether the Poll is private or not.

        }

        returns:

        {

            "poll_id": ID of the created Poll.

        }"""

        poll_dto = PollDto.from_json({**request.json, "userId": user.id})
        try:
            Poll.prisma().create(data=poll_dto.to_insertable())
            poll = Poll.prisma().find_first(
                where={
                    "title": poll_dto.title,
                    "userId": user.id,
                }
            )
            return make_response({"pollId": poll.id})
        except Exception:
            raise BadRequest("couldn't create poll from request")


polls_api.add_resource(PollResource, "")
polls_api.add_resource(UniquePollItems, "/<poll:poll>/pollitems")
