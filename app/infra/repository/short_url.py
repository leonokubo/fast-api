from abc import ABC
from typing import ClassVar

from sqlalchemy.future import select

from app.domain.entity.short_url import ShortURLDB
from app.infra.config import setting, async_session


class Repository(ABC):
    _t_entity: ClassVar

    # @property
    # def session(self):
    #     return setting.session().select(self._t_entity)
    #
    # def save(self, data: dict):
    #     self.session.add(data)
    #     return data

    async def get(self):
        async with async_session() as session:
            q = select(self._t_entity)
            result = await session.execute(q)
            return result.scalars().all()


class ShortUrlRepo(Repository):
    _t_entity = ShortURLDB
