import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def clean_data(ticker):

    file_path = os.path.join(DATA_DIR, f"{ticker}_data.csv")

    print(f"Cleaning data for {ticker}...")


    df = pd.read_csv(file_path, skiprows=[1,2])


    df = df.rename(columns={"Price": "Date"})

    df["Date"] = pd.to_datetime(df["Date"])

    numeric_cols = ["Close", "High", "Low", "Open", "Volume"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")


    df = df.dropna()

    df = df.drop_duplicates(subset="Date")

    float_cols = ["Close", "High", "Low", "Open"]
    df[float_cols] = df[float_cols].round(4)


    df = df.sort_values("Date").reset_index(drop=True)

    output_path = os.path.join(DATA_DIR, f"{ticker}_cleaned.csv")
    df.to_csv(output_path, index=False)

    print(f"Cleaned data saved to {output_path}")
    print(df.dtypes)

    return df
