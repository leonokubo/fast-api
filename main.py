from fastapi import FastAPI

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
    ...


@app.on_event('shutdown')
async def on_shutdown() -> None:
    ...
