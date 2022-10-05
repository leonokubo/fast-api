import abc

from app.infra.repository.short_url import ShortUrlRepo


class Handler(abc.ABC):
    ...


class ShortURL(Handler):

    @staticmethod
    async def get() -> dict:
        c = ShortUrlRepo()
        x = await c.get()
        return x

    @staticmethod
    def post(name) -> dict:
        return {"name": name}
