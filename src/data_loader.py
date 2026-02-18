# data_loader.py

import os
import matplotlib
import pandas as pd
import yfinance as yf
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")  # better plot style

def fetch_and_plot_data(ticker: str, period="5y", interval="1d"):
   
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Download data
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period=period, interval=interval)
    
    if data.empty:
        print("No data fetched. Check ticker symbol or network.")
        return
    
    # Save CSV
    csv_path = f"data/{ticker}_data.csv"
    data.to_csv(csv_path)
    print(f"Data saved to {csv_path}")
    
    # Plot Closing price
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Close'], label="Close Price")
    plt.title(f"{ticker} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    price_plot_path = f"data/{ticker}_price.png"
    plt.savefig(price_plot_path)
    plt.close()
    print(f"Price plot saved to {price_plot_path}")
    
    # Compute daily returns
    data['Return'] = data['Close'].pct_change()
    
    # Plot Returns
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Return'], label="Daily Return")
    plt.title(f"{ticker} Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Return")
    plt.legend()
    plt.tight_layout()
    return_plot_path = f"data/{ticker}_returns.png"
    plt.savefig(return_plot_path)
    plt.close()
    print(f"Returns plot saved to {return_plot_path}")
    
    print("Data fetching and plotting complete.")
