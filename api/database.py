"""Module for setting up Prisma"""

from prisma import Prisma, register

db = Prisma()

register(db)


def connect_to_db():
    """Wrapper function for connecting to the database"""
    db.connect()
