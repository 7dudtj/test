# FutureWarning: Indexing a DataFrame with a datetimelike index using a single string to slice the rows, 
# like `frame[string]`, is deprecated and will be removed in a future version. 
# Use `frame.loc[string]` instead.

import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
# df = df['2018'] << old code
df = df.loc['2018'] # new code
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)
ror = df['ror'].cumprod()[-2]
print(ror)

df.to_excel("btc.xlsx")