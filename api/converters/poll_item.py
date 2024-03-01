from werkzeug.routing import BaseConverter
from werkzeug.exceptions import NotFound
from prisma.models import PollItem


class PollItemConverter(BaseConverter):
    def to_python(self, poll_item_id):
        poll_item = PollItem.prisma().find_first(where={"id": poll_item_id})
        if poll_item is None:
            raise NotFound
        return poll_item.id

    def to_url(self, poll_item):
        return poll_item.id
