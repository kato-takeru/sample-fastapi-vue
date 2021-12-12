# from datetime import date
from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class TrendBase(BaseModel):
    id: int
    keyword: str = Field('', example="鬼滅の刃")

    class Config:
        orm_mode = True


class TrendDetail(TrendBase):
    data: Dict = Field(None, example="")

    class Config:
        orm_mode = True
