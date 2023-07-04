import pandas as pd
import pandas_ta as ta
import yfinance as yf

stocks = 'TATAMOTORS.NS BHEL.NS'

df = yf.download(stocks, '2023-06-01', interval='1d',)

technicals = ['sma10', 'sma25', 'vwma']
tickers = stocks.split(' ')


# # Calculate Heikin-Ashi candles
# for ticker in tickers:
#     df[('ha_open', ticker)], df[('ha_high', ticker)], df[('ha_low', ticker)], df[('ha_close', ticker)] = ta.ha(df.loc[:, ('Open', ticker)], df.loc[:, ('High', ticker)], df.loc[:, ('Low', ticker)], df.loc[:, ('Close', ticker)])
#
#     print("ha_open={}, ha_close={}".format(df['ha_open'], df['ha_close']))

for ticker in tickers:
  for t in technicals:
    if t[:2] == 'sma':
      l = int(t[3:])
      print(l)
      technical = ta.ha(df.loc[:,('Close', ticker)])
      df[(t, ticker)] = technical
      print(technical)