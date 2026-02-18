# main.py

from src.data_loader import fetch_and_plot_data

def main():
    print("=== Trading Bot Data Fetcher ===")

    tickers_input = input("Enter ticker symbols (comma separated, e.g., AAPL,GOOGL,MSFT): ")
    
    # Split, strip spaces, convert to uppercase
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
    
    if not tickers:
        print("No tickers entered. Exiting.")
        return
    
    for ticker in tickers:
        try:
            fetch_and_plot_data(ticker, period="5y", interval="1d")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    print("All requested data fetched and plots saved.")

if __name__ == "__main__":
    main()
