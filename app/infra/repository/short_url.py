from abc import ABC
from typing import ClassVar

from app.domain.entity.short_url import ShortURLDB
from app.infra.config import session


class Repository(ABC):
    _t_entity: ClassVar

    @property
    def session(self):
        return session

    def save(self, data: dict):
        self.session.add(data)
        return data


class ShortUrlRepo(Repository):
    _t_entity = ShortURLDB
