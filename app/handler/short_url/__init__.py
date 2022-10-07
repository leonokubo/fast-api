import abc
from typing import ClassVar

from app.application import ShortUrlApplication


class Handler(abc.ABC):
    _app: ClassVar

    def __init__(self):
        self.app = self._app()


class ShortURL(Handler):
    _app = ShortUrlApplication

    async def get(self) -> list:
        """
        Get all short url
        :return: []
        """
        response = await self.app.get()
        return response

    async def post(self, body) -> dict:
        response = await self.app.add(body)
        return response
