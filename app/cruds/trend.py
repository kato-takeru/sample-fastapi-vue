from pytrends.request import TrendReq
from models import Trend
from sqlalchemy.orm import Session


def read_trends(db: Session):
    items = db.query(Trend).all()
    return items


# def read_trend(db: Session, trend_id: int):
#     return db.query(Trend).first()


def read_trend(db: Session, trend_id: int):
    trend = db.query(Trend).filter(Trend.id == trend_id).first()
    keyword = trend.keyword

    pytrend = TrendReq()
    kw_list = [keyword]
    pytrend.build_payload(kw_list, geo='JP')

    df = pytrend.interest_over_time()
    df = df.drop('isPartial', axis=1)
    df = df.reset_index().values.tolist()

    param = {
        "id": trend.id,
        "keyword": keyword,
        "value": df
    }

    return param
