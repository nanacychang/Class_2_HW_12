import requests
from bs4 import BeautifulSoup
import pandas as pd
import statistics

stock_code='0056'

url_price=f'https://goodinfo.tw/StockInfo/ShowK_Chart.asp?STOCK_ID={stock_code}&CHT_CAT2=YEAR'

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36', 'referer': f'https://goodinfo.tw/StockInfo/Stockdetail.asp?STOCK_ID={stock_code}'}
#歷年股價估算法

resp_price=requests.get(url_price, headers=headers)
resp_price.encoding='utf-8'

raw_html_price=resp_price.text

price_soup=BeautifulSoup(raw_html_price, 'html.parser')

price_list=[]

for r in range(0,10):
  price_list.append(price_soup.select(f'#row{r} td nobr')[5].text)

print('10yr_price_list', price_list)

max_price=max(price_list)
min_price=min(price_list)

print('10yr_max_price:', max_price)
print('10yr_min_price:', min_price)

#存成csv檔
df_price=pd.DataFrame({'10yr_price_list': price_list})
df_price.to_csv(f'price_{stock_code}.csv', index=False)
