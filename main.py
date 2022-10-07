import time

import aioredis
from fastapi import FastAPI, Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.router.short_url import router

app = FastAPI(
    title="Short URL",
    version="0.0.1",
    description="Short URL - Fast Api",
    routes=router.routes
)
app.include_router(router)


@app.on_event('startup')
async def on_startup() -> None:
    redis = aioredis.from_url(
        url="redis://localhost",
        encoding="utf8",
        decode_responses=True,
        password="a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2",
        db=3
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


@app.on_event('shutdown')
async def on_shutdown() -> None:
    ...


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
