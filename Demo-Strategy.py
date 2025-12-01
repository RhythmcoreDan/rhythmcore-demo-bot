"""
Demo Strategy Module
---------------------
A minimal example of how I structure trading logic inside a bot system.
This version uses simple moving averages to demonstrate:
- clean architecture
- indicator calculation
- entry/exit logic
"""

import pandas as pd

def compute_signals(df: pd.DataFrame) -> pd.DataFrame:
    df['ma_fast'] = df['close'].rolling(window=10).mean()
    df['ma_slow'] = df['close'].rolling(window=30).mean()

    df['signal'] = 0
    df.loc[df['ma_fast'] > df['ma_slow'], 'signal'] = 1
    df.loc[df['ma_fast'] < df['ma_slow'], 'signal'] = -1

    return df


def generate_trades(df: pd.DataFrame):
    df = compute_signals(df)
    trades = []

    last_signal = 0
    for idx, row in df.iterrows():
        if row['signal'] != last_signal:
            trades.append({
                'time': row['time'],
                'price': row['close'],
                'signal': row['signal'],
            })
            last_signal = row['signal']

    return trades


if __name__ == "__main__":
    print("Demo strategy file. Run sample_backtest.py to see it in action.")
