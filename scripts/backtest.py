import pandas as pd

def backtest(df):
    initial_capital = 100000
    df['portfolio_value'] = initial_capital * (1 + df['strategy_returns']).cumprod()
    return df

if __name__ == "__main__":
    df = pd.read_csv('data\strategy_data.csv')
    df = backtest(df)
    df.to_csv('data\backtest_results.csv', index=False)
