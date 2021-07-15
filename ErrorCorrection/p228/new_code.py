# 상장 5일차 이하라 전일 5일 이동평균을 구할수 없는 경우를 위한 Error Handling

import pybithumb

def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    price = pybithumb.get_current_price(ticker)
    last_ma5 = ma5[-2]
    if price > last_ma5:
        return True
    else:
        return False

tickers = pybithumb.get_current_price("ALL")
for ticker in tickers:
    try:
        is_bull = bull_market(ticker)
    except:
        continue
    if is_bull:
        print(ticker, "상승장")
    else:
        print(ticker, "하락장")s
