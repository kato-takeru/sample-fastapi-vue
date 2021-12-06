from database import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from .mixins import TimestampMixin  # 後述


class Trend(Base, TimestampMixin):
    __tablename__ = 'trends'

    id = Column(Integer, primary_key=True, autoincrement=True)
    keyword = Column(String(128), nullable=False)
    value = Column(String(10000), nullable=True)
