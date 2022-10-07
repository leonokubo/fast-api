from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import validates, relationship
from sqlalchemy.schema import FetchedValue

from app.domain.entity import Entity


class ShortURLDB(Entity):
    __tablename__ = "shorturl"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    url: str = Column(String(200))
    hash_code: int = Column("hash", String(45), index=True)
    url_md5 = Column(String(32), unique=True)
    created_at = Column(TIMESTAMP, server_default=FetchedValue(), index=True)
    updated_at = Column(TIMESTAMP, server_default=FetchedValue(), index=True)
    deleted_at = Column(TIMESTAMP, index=True)
