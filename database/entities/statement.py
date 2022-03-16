import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

from database import Entity
# from database.entities.currency import ECurrency


class Statement(Entity):
    __tablename__ = 'statement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=True)
    status = Column(String, nullable=True)
    name = Column(String, nullable=True)
    account = Column(String, ForeignKey('account.number'))
    date = Column(DateTime, default=datetime.datetime.now())

    def __eq__(self, other):
        return isinstance(other, Statement) and self.id == other.id
