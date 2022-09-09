import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from sqlalchemy.pool import NullPool

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "admin")
DB_NAME = os.getenv("DB_NAME", "backoffice_jobs")
DRIVE = os.getenv("DRIVE", "mysql")
INSTANCE = os.getenv("INSTANCE", "")

db_config = {
    "poolclass": NullPool
    # "pool_size": 10,
    # "max_overflow": -1,
    # "pool_timeout": 60,
    # "pool_recycle": 1800,
    # "pool_pre_ping": True
}


class DB(object):
    def __init__(self):
        self._engine = None
        self._session = None

    @property
    def engine(self):
        self._engine = create_engine(
            f"{DRIVE}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4",
            **db_config
        )
        return self._engine

    @property
    def session(self) -> Session:
        self._session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        return self._session()


session = DB().session
meta = MetaData()
Base = declarative_base()
