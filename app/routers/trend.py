import cruds.trend as crud
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
# schemas の中身は後述
from schemas.trend import TrendBase as TrendSchema
from schemas.trend import TrendDetail as TrendDetailSchema
from typing import List
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/', response_model=List[TrendSchema])
def read_trends(db: Session = Depends(get_db)):
    return crud.read_trends(db)


@router.get('/{trend_id}', response_model=TrendDetailSchema)
def read_trend(trend_id: int, db: Session = Depends(get_db)):
    trend = crud.read_trend(db, trend_id=trend_id)
    if trend is None:
        raise HTTPException(status_code=404, detail="Trend not found")
    return trend
