from abc import ABC
from typing import ClassVar

from sqlalchemy.exc import IntegrityError
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

    async def add(self, base: Entity) -> dict:
        async with async_session() as session:
            try:
                session.add(base)
                await session.commit()
                return base
            except IntegrityError:
                await session.rollback()
                return {}


class ShortUrlRepo(Repository):
    _t_entity = ShortURLDB

    async def add(self, base: Entity) -> dict:
        async with async_session() as session:
            try:
                session.add(base)
                await session.commit()
                return base.to_json()
            except IntegrityError:
                await session.rollback()
                qry = select(self._t_entity).where(self._t_entity.url_md5 == base.url_md5)
                result = await session.execute(qry)
                return result.scalars().one().to_json()
