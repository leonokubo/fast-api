import os

from pydantic import BaseSettings
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "admin")
DB_NAME = os.getenv("DB_NAME", "shorturl")
DRIVE = os.getenv("DRIVE", "mysql+asyncmy")
INSTANCE = os.getenv("INSTANCE", "")

db_config = {
    "pool_size": 10,
    "max_overflow": -1,
    "pool_timeout": 60,
    "pool_recycle": 1800,
    "pool_pre_ping": True
}

engine: AsyncEngine = create_async_engine(
    f"{DRIVE}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4", **db_config
)


class Settings(BaseSettings):
    DBBase = declarative_base()

    @staticmethod
    def get_session() -> AsyncSession:
        session = sessionmaker(
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession,
            bind=engine
        )

        return session()


setting = Settings()
