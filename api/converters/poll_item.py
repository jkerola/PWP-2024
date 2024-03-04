"""Module containing the PollItemConverter"""

from werkzeug.routing import BaseConverter
from werkzeug.exceptions import NotFound
from prisma.models import PollItem


class PollItemConverter(BaseConverter):
    """Converts the poll_item_id url-parameter to PollItem"""

    def to_python(self, value):
        poll_item = PollItem.prisma().find_first(where={"id": value})
        if poll_item is None:
            raise NotFound
        return poll_item.id

    def to_url(self, value):
        return value.id
