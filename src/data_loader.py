import os
import matplotlib
import yfinance as yf
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

def fetch_and_plot_data(ticker: str, period: str, interval: str):

    if not os.path.exists("data"):
        os.makedirs("data")

    print(f"Fetching data for {ticker}...")

    data = yf.download(ticker, period=period, interval=interval)

    if data.empty:
        print("No data fetched. Check ticker symbol.")
        return

    data.reset_index(inplace=True)

    # Save CSV
    csv_path = f"data/{ticker}_data.csv"
    data.to_csv(csv_path, index=False)

    print(f"Data saved to {csv_path}")

    # PRICE PLOT
    plt.figure(figsize=(12,6))
    plt.plot(data["Date"], data["Close"], label="Close Price")
    plt.title(f"{ticker} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()

    price_plot_path = f"data/{ticker}_price.png"
    plt.savefig(price_plot_path)
    plt.close()

    print(f"Price plot saved to {price_plot_path}")

    # RETURNS
    data["Return"] = data["Close"].pct_change()

    plt.figure(figsize=(12,6))
    plt.plot(data["Date"], data["Return"], label="Daily Return")
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
