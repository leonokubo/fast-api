import abc
from typing import Any as AnyEntity
import hashlib
from app.domain.entity.short_url import ShortURLDB
from app.infra.repository.short_url import ShortUrlRepo


class ApplicationABC(abc.ABC):
    ...


class ShortUrlApplication(ApplicationABC):

    @staticmethod
    async def get(_id: int = None):
        response = await ShortUrlRepo().get()
        return response

    @staticmethod
    async def add(body: AnyEntity):
        md5 = hashlib.md5(body.url.encode('utf-8')).hexdigest()
        response = await ShortUrlRepo().add(ShortURLDB(url=body.url, url_md5=md5))
        return response
