"""Module containing the PollItemConverter"""

from werkzeug.routing import BaseConverter
from werkzeug.exceptions import NotFound
from prisma.models import PollItem

# Impressed by the converter example found in exercise 2
# https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/implementing-rest-apis-with-flask/
class PollItemConverter(BaseConverter):
    """Converts the poll_item_id url-parameter to PollItem"""

    def to_python(self, value):
        poll_item = PollItem.prisma().find_unique(where={"id": value})
        if poll_item is None:
            raise NotFound
        return poll_item

    def to_url(self, value):
        return value.id
