from database import SessionLocal
from models import Item, Sku, Trend

db = SessionLocal()


def seed():
    skuDatas = [
        {
            'sku_code': 'et02900034611111',
            'whosale_price': 3220,
            'price': 9000,
        },
        {
            'sku_code': 'et02900034611112',
            'whosale_price': 3220,
            'price': 9000,
        },
        {
            'sku_code': 'et02900034611113',
            'whosale_price': 3220,
            'price': 9000,
        },
    ]
    skus = [
        Sku(
            sku_code=skuData['sku_code'],
            whosale_price=skuData['whosale_price'],
            price=skuData['price'],
        ) for skuData in skuDatas
    ]
    item = Item(item_number='et0290003461')
    item.skus = skus  # リレーションも丸ごと表現できる

    trends = [
        Trend(keyword='鬼滅の刃'),
        Trend(keyword='進撃の巨人'),
        Trend(keyword='ハイキュー'),
    ]

    for trend in trends:
        db.add(trend)
        db.commit()

    db.add(item)
    db.commit()


if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()
