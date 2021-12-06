# from datetime import date
from pydantic import BaseModel, Field
from typing import Optional, List


class TrendBase(BaseModel):
    id: int
    keyword: str = Field('', example="鬼滅の刃")

    class Config:
        orm_mode = True


class TrendDetail(TrendBase):
    value: List[List] = Field(None, example="")

    class Config:
        orm_mode = True
