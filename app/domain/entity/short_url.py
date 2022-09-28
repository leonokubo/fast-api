from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import validates
from sqlalchemy.schema import FetchedValue

from app.domain.entity import Entity


class ShortURLDB(Entity):
    __tablename__ = "shorturl"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    hash: int = Column(String(45), unique=True)
    url: str = Column(String(72))
    created_at = Column(TIMESTAMP, server_default=FetchedValue(), index=True)
    updated_at = Column(TIMESTAMP, server_default=FetchedValue(), index=True)
    deleted_at = Column(TIMESTAMP, index=True)

    @validates('hash')
    def _valid_hash(self, key, value):
        ...
