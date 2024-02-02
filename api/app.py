from flask import Flask
from prisma import Prisma, register


db = Prisma()
db.connect()
register(db)
app = Flask(__name__)
