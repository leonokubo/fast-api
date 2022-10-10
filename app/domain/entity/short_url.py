import short_url as lib_short_url
from sqlalchemy import Column, String, Integer, TIMESTAMP, text
from sqlalchemy.sql import func

from app.domain.entity import Entity


class ShortURLDB(Entity):
    __tablename__ = "shorturl"
    __hide_attr__ = ()
    __show_ppt__ = ()

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    url: str = Column(String(200))
    url_md5 = Column(String(32), unique=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), index=True, )
    updated_at = Column(TIMESTAMP, server_default=text('NULL ON UPDATE CURRENT_TIMESTAMP'), index=True)
    deleted_at = Column(TIMESTAMP, index=True)

    def to_json(self):
        return {
            "hash": lib_short_url.encode_url(self.id),
            "url": self.url
        }
