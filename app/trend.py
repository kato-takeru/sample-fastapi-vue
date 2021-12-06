from pytrends.request import TrendReq

pytrend = TrendReq()
kw_list = ["Twitter"]
pytrend.build_payload(kw_list, geo='JP')

df = pytrend.interest_over_time()
df.drop('isPartial', axis=1)

print(df)
