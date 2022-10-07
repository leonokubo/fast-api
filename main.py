import time

from fastapi import FastAPI, Request

from app.infra.cache.fastapi_cache import CacheApp
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
    cache = CacheApp()
    cache.start_app()


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
