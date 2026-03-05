import pandas as pd

import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "AAPL_data.csv")

df = pd.read_csv(file_path, skiprows=[1, 2])

# Drop first 2 unwanted rows (Ticker + Date row)
df = df.drop([1, 2]).reset_index(drop=True)

# Rename first column properly
df = df.rename(columns={"Price": "Date"})

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Convert numeric columns to float
numeric_cols = ["Close", "High", "Low", "Open", "Volume"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# Remove duplicates (based on Date)
df = df.drop_duplicates(subset="Date")

# Round float columns to 4 decimal places
float_cols = ["Close", "High", "Low", "Open"]
df[float_cols] = df[float_cols].round(4)

# Sort by date (important for ML)
df = df.sort_values("Date").reset_index(drop=True)

print(df.head())

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)