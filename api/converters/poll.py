"""Module containing the PollConverter"""

from werkzeug.routing import BaseConverter
from werkzeug.exceptions import NotFound
from prisma.models import Poll

# Impressed by the converter example found in exercise 2
# https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/implementing-rest-apis-with-flask/
class PollConverter(BaseConverter):
    """Converts the poll_id url-parameter into a Poll"""

    def to_python(self, value):
        poll = Poll.prisma().find_first(where={"id": value})
        if poll is None:
            raise NotFound
        return poll

    def to_url(self, value):
        return value.id
