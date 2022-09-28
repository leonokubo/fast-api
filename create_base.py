import asyncio

from app.domain.entity.short_url import ShortURLDB
from app.infra.config import setting, engine

__all__ = [ShortURLDB]


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(setting.DBBase.metadata.create_all)


asyncio.run(create_table())
