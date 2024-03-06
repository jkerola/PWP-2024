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
    """Route resource representing a unique poll"""

    method_decorators = {
        "delete": [requires_authentication],
        "patch": [requires_authentication],
    }

    def get(self, poll: Poll):
        """Get a single poll by id"""
        return make_response(poll.model_dump(exclude=["user"]))

    def delete(self, poll: Poll, user: User):
        """Delete a poll"""
        if poll.userId == user.id:
            Poll.prisma().delete(where={"id": poll.id})
            return make_response("", 204)
        return make_response("", 403)

    def patch(self, poll: Poll, user: User):
        """Update a poll"""
        if poll.userId == user.id:
            try:
                data = request.json
                # TODO: proper verification needed
                updated = Poll.prisma().update(
                    where={"id": poll.id, "userId": user.id},
                    data={
                        "title": data.get("title") or poll.title,
                        "description": data.get("description") or poll.description,
                        "multipleAnswers": data.get("multipleAnswers")
                        or poll.multipleAnswers,
                        "private": data.get("private") or poll.private,
                        "expires": data.get("expires") or poll.expires,
                    },
                )
                return make_response(updated.model_dump(exclude=["user", "items"]), 201)
            except Exception as e:
                print(e)
                raise BadRequest("couldn't update poll")

        return make_response("", 403)


class PollCollection(Resource):
    """Resource representing all polls"""

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
            poll = Poll.prisma().create(data=poll_dto.to_insertable())
            return make_response(poll.model_dump(exclude=["user", "items"]))
        except Exception:
            raise BadRequest("couldn't create poll from request")


polls_api.add_resource(PollCollection, "")
polls_api.add_resource(PollResource, "/<poll:poll>")
polls_api.add_resource(UniquePollItems, "/<poll:poll>/pollitems")
