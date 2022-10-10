from app.infra.config import setting


class Entity(setting.DBBase):
    __abstract__ = True
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8mb4"}
