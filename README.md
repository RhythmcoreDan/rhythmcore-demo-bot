Rhythmcore Demo Bot

A minimal, clean example of the architecture and logic I use when building automated trading systems.
This demo includes a simple moving-average strategy, a backtest runner, and a lightweight project structure that mirrors my production-level work.

This repository is intentionally small and safe — the full RhythmCore system includes real-time data ingestion, emotional-state modeling, regime detection, execution engines, and monitoring pipelines.

🚀 Features

Clean, modular Python structure

Demo strategy module (demo_strategy.py)

Example backtest runner (sample_backtest.py)

Sample OHLC dataset (sample_prices.csv)

Clear entry/exit signal logic

Easy to extend into more complex systems

📂 Project Structure
rhythmcore-demo-bot/
│
├── demo_strategy.py        # Indicator + signal logic
├── sample_backtest.py      # Simple backtest runner
├── sample_prices.csv       # Example candle data
└── README.md               # Documentation

🧠 How It Works
1. Compute Signals

The strategy calculates two moving averages (fast + slow) and generates BUY/SELL signals based on crossovers.

2. Generate Trades

Whenever the signal changes, the script logs a trade event with timestamp and price.

3. Run a Backtest

Use the included sample CSV to simulate basic strategy behavior:

python sample_backtest.py

📈 Output Example
=== Backtest Results ===
2024-01-03 | BUY @ 1.1040
2024-01-10 | SELL @ 1.1110

Backtest complete.

🔧 Tech Stack

Python

Pandas

Basic technical indicators

CSV data ingestion

📬 About This Repo

This repo is a public, simplified demonstration of my coding style and approach to algo-engineering.
My full projects include:

Real-time APIs

Execution engines

Emotional/behavioral market modeling

Regime maps

Multi-feed Discord/streaming output

Backtesting + forward-testing pipelines

If you'd like to collaborate or see more, feel free to reach out.
