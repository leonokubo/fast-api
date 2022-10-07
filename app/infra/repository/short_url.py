from abc import ABC
from typing import ClassVar

import short_url as lib_short_url
from sqlalchemy.future import select

from app.domain.entity import Entity
from app.domain.entity.short_url import ShortURLDB
from app.infra.config import async_session


class Repository(ABC):
    _t_entity: ClassVar

    async def get(self):
        async with async_session() as session:
            qry = select(self._t_entity)
            result = await session.execute(qry)
            return result.scalars().all()

    @staticmethod
    async def add(base: Entity):
        async with async_session() as session:
            session.add(base)
            await session.flush()
            base.hash_code = lib_short_url.encode_url(base.id)
            await session.commit()


class ShortUrlRepo(Repository):
    _t_entity = ShortURLDB
