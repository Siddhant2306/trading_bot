# main.py
import pandas as pd
import matplotlib.pyplot as plt

#from src.strategy import compute_statistics, generate_signals
from src.data_loader import fetch_and_plot_data
from src.data_cleaner import clean_data
from src.backtester import backtest_strategy
from src.strategy_statistical import compute_returns
from src.walk_forward_test import walk_forward_test
   

def main():
    print("=== Trading Bot Data Fetcher ===")

    tickers_input = input("Enter ticker symbols (comma separated, e.g., AAPL,GOOGL,MSFT): ")
    period_input = input("Enter your periods in years: ")
    interval_input = input("Enter the interval: ")

    # Split, strip spaces, convert to uppercase
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
    
    if not tickers:
        print("No tickers entered. Exiting.")
        return
    
    for ticker in tickers:
        try:
            fetch_and_plot_data(ticker, period=period_input, interval=interval_input)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    run_strategy(ticker)
    print("All requested data fetched and plots saved.")

def run_strategy(ticker):

    #path = f"data/{ticker}_data.csv"

    #df = pd.read_csv(path, index_col="Date", parse_dates=True)

    df = clean_data(ticker)
    df = compute_returns(df)


    initial_capital = int(input("Enter your initial amount to trade:"))
    traindata = int(input("Enter number of years u want to train:"))

    df = walk_forward_test(df,traindata,initial_capital)

    #print(f"Final portfolio value: {final_value}")
    df.to_csv(f"data/{ticker}_strategy_output.csv")

    plt.figure(figsize=(12,6))

    plt.plot(df.index, df["Portfolio_Value"], label="Portfolio")

    buy_signals = df[df["Signal"] == 1]
    sell_signals = df[df["Signal"] == -1]

    plt.scatter(buy_signals.index, buy_signals["Portfolio_Value"], marker="^")
    plt.scatter(sell_signals.index, sell_signals["Portfolio_Value"], marker="v")

    plt.title("Strategy Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()

    plt.savefig(f"data/{ticker}_equity_curve.png")
    plt.close()

if __name__ == "__main__":
    main()
