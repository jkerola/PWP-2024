from prisma import Prisma, register


db = Prisma()

register(db)


def connect_to_db():
    db.connect()
