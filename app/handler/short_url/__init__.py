import abc


class Handler(abc.ABC):
    ...


class ShortURL(Handler):

    @staticmethod
    def get() -> dict:
        return {}

    @staticmethod
    def post(name) -> dict:
        return {"name": name}
