import pandas as pd
import numpy as np


def compute_returns(df):

    df["Return"] = df["Close"].pct_change()
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year

    return df


def compute_yearly_statistics(df, k=3):

    stats = df.groupby("Year")["Return"].agg(["mean", "median", "std"])

    # estimate mode using histogram
    mode_values = []

    for year in stats.index:

        year_returns = df[df["Year"] == year]["Return"].dropna()

        hist, bins = np.histogram(year_returns, bins=50)
        idx = np.argmax(hist)

        mode = (bins[idx] + bins[idx+1]) / 2
        mode_values.append(mode)

    stats["mode"] = mode_values

    stats["Lower"] = stats["median"] - k * stats["std"]
    stats["Upper"] = stats["median"] + k * stats["std"]

    return stats


def compute_overlap_band(stats):

    lower = stats["Lower"].max()
    upper = stats["Upper"].min()

    # FIX: prevent impossible overlap
    if lower >= upper:

        # fallback to average band
        lower = stats["Lower"].mean()
        upper = stats["Upper"].mean()

    return lower, upper


def generate_signals(df, lower, upper):

    df["Signal"] = 0

    df.loc[df["Return"] < lower, "Signal"] = 1
    df.loc[df["Return"] > upper, "Signal"] = -1

    return df
