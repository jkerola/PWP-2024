from prisma import Prisma, register


db = Prisma()
db.connect()
register(db)
