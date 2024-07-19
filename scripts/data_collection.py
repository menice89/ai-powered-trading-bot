import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

def fetch_historical_data(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date)
    df = df.rename(columns={
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'adjusted_close',
        'Volume': 'volume'
    })
    return df

def preprocess_data(df):
    df.fillna(method='ffill', inplace=True)
    df['returns'] = df['close'].pct_change()
    df['moving_avg'] = df['close'].rolling(window=20).mean()
    return df.dropna()

if __name__ == "__main__":
    symbol = 'AAPL'
    start_date = '2020-01-01'
    end_date = datetime.today().strftime('%Y-%m-%d')
    df = fetch_historical_data(symbol, start_date, end_date)
    df = preprocess_data(df)
    df.to_csv('data\preprocessed_data.csv', index=False)
