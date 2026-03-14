import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def clean_data(ticker):

    file_path = os.path.join(DATA_DIR, f"{ticker}_data.csv")

    print(f"Cleaning data for {ticker}...")

    # Read CSV and skip unwanted rows
    df = pd.read_csv(file_path, skiprows=[1,2])

    # Rename first column
    df = df.rename(columns={"Price": "Date"})

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"])

    # Convert numeric columns
    numeric_cols = ["Close", "High", "Low", "Open", "Volume"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # Remove bad rows
    df = df.dropna()

    # Remove duplicate dates
    df = df.drop_duplicates(subset="Date")

    # Round floats
    float_cols = ["Close", "High", "Low", "Open"]
    df[float_cols] = df[float_cols].round(4)

    # Sort by date
    df = df.sort_values("Date").reset_index(drop=True)

    # Save cleaned file
    output_path = os.path.join(DATA_DIR, f"{ticker}_cleaned.csv")
    df.to_csv(output_path, index=False)

    print(f"Cleaned data saved to {output_path}")
    print(df.dtypes)

    return df
