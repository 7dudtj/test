# 우회 코드

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}
response = requests.get(url, headers=headers)
html = bs(response.text, "lxml")
table = html.select("table")
table = pd.read_html(str(table))
df = table[0].dropna()
print(df)
