import pybithumb
import numpy as np

def get_ror(k):
    df = pybithumb.get_ohlcv("BTC")
    # df = df.loc['2021-07']
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] >= df['target'], df['close'] / df['target'] - fee, 1)

    ror = df['ror'].cumprod()[-2]
    return ror

for k in np.arange(0.1, 1.0, 0.01):
    ror = get_ror(k)
    print("%.2f %f" % (k, ror))