"""
Sample Backtest Runner
----------------------
This script loads a small CSV of OHLC data, runs the demo strategy,
and prints formatted trade events.

This is only a structural example — the full RhythmCore system includes:
- real-time feeds
- emotional engine
- regime detection
- execution APIs
- Discord streaming
"""

import pandas as pd
from demo_strategy import generate_trades

def run_backtest():
    df = pd.read_csv("sample_prices.csv")

    trades = generate_trades(df)

    print("=== Backtest Results ===")
    for t in trades:
        direction = "BUY" if t['signal'] == 1 else "SELL"
        print(f"{t['time']} | {direction} @ {t['price']}")

    print("\nBacktest complete.")


if __name__ == "__main__":
    run_backtest()
