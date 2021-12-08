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
    xAxis = df.filter(items=['date'], axis='columns')

    data = {
        'xAxis': xAxis
    }

    print(data)

    # param = {
    #     "id": trend.id,
    #     "keyword": keyword,
    #     "value": data
    # }

    # return param
