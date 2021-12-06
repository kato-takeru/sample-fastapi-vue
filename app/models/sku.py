from database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER as Integer
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin  # 後述


class Sku(Base, TimestampMixin):
    __tablename__ = 'skus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(
        Integer,
        ForeignKey("items.id", onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False
    )
    sku_code = Column(String(128), nullable=True)
    whosale_price = Column(Integer(unsigned=True))
    price = Column(Integer(unsigned=True))

    item = relationship('Item', back_populates='skus')
