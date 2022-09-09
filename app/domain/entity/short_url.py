from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.schema import FetchedValue

from app.domain.entity import Entity


class ShortURLDB(Entity):
    __tablename__ = "shorturl"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    hash: int = Column(Integer(), ForeignKey("state.id"), nullable=False)
    url: str = Column(String(72))
    created_at = Column(TIMESTAMP, server_default=FetchedValue())
    updated_at = Column(TIMESTAMP, server_default=FetchedValue())
    deleted_at = Column(TIMESTAMP)
