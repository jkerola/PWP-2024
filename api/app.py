import asyncio
from flask import Flask
from prisma import Prisma, register


db = Prisma()
asyncio.run(db.connect())
register(db)
app = Flask(__name__)
