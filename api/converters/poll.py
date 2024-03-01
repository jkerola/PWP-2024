from werkzeug.routing import BaseConverter
from werkzeug.exceptions import NotFound
from prisma.models import Poll


class PollConverter(BaseConverter):
    def to_python(self, poll_id):
        poll = Poll.prisma().find_first(where={"id": poll_id})
        if poll is None:
            raise NotFound
        return poll.id

    def to_url(self, poll):
        return poll.id
