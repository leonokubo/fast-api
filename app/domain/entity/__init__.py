from app.infra.config import Base


class Entity(Base):
    __abstract__ = True
    __hide_attr__ = ()
    __show_ppt__ = ()
