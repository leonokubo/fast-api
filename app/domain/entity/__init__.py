from app.infra.config import setting


class Entity(setting.DBBase):
    __abstract__ = True
    __hide_attr__ = ()
    __show_ppt__ = ()
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8mb4"}
