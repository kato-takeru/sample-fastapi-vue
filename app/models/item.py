from database import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin  # 後述


class Item(Base, TimestampMixin):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_number = Column(String(128), nullable=True)
    trend_id = Column(
        Integer,
        ForeignKey("trends.id", onupdate='CASCADE', ondelete='CASCADE'),
        nullable=True
    )

    skus = relationship('Sku', back_populates='item')
    trend = relationship('Trend')
