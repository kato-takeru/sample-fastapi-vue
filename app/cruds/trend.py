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

    data = {
        'xAxis': df.index.date.tolist(),
        'series': df[keyword].tolist()
    }

    return {
        "id": trend.id,
        "keyword": keyword,
        "data": data
    }
