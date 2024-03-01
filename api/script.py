from prisma.models import User, Poll, PollItem
import datetime
from database import connect_to_db

connect_to_db()
d = datetime.datetime.now() + datetime.timedelta(days=30)
user = User.prisma().find_first()
poll = Poll.prisma().create(
    {
        "userId": user.id,
        "title": "election",
        "description": "vote for the next president",
        "expires": d,
    }
)
PollItem.prisma().create({"description": "stubb", "pollId": poll.id})
PollItem.prisma().create({"description": "haavisto", "pollId": poll.id})
PollItem.prisma().create({"description": "putin", "pollId": poll.id})
