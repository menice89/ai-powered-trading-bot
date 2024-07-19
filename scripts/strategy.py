import pandas as pd
import numpy as np

def momentum_strategy(df):
    df['signal'] = np.where(df['close'] > df['moving_avg'], 1, -1)
    df['strategy_returns'] = df['signal'].shift(1) * df['returns']
    return df

if __name__ == "__main__":
    df = pd.read_csv('data\preprocessed_data.csv')
    df = momentum_strategy(df)
    df.to_csv('data\strategy_data.csv', index=False)
