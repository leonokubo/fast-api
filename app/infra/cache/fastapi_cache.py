import aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.infra.config import REDIS_HOST, REDIS_PASSWORD, REDIS_DB


class CacheApp:
    redis: aioredis

    def __init__(self):
        self.redis = aioredis.from_url(
            url=F"redis://{REDIS_HOST}",
            encoding="utf8",
            decode_responses=True,
            password=REDIS_PASSWORD,
            db=REDIS_DB
        )

    def start_app(self):
        FastAPICache.init(RedisBackend(self.redis), prefix="short-url")
