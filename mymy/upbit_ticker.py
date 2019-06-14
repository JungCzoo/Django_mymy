import pyupbit
import pandas as pd
import json

def ticker():
    krw_tickers = pyupbit.get_tickers(fiat="KRW")
    price = pyupbit.get_current_price(krw_tickers)
    return price


def dict_date(coin_name):
    df = pyupbit.get_ohlcv(coin_name)
    df = pd.DataFrame(df)
    df['date'] = df.index
    df['date'] = df['date'].dt.date
    items = ['open', 'high', 'low', 'close']
    for item in items:
        df[item] = df[item].astype(str)
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df_dict = df[['date', 'open', 'high', 'low', 'close']].to_dict('records')
    return df_dict
