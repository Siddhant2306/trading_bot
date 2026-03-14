import pandas as pd
from src.strategy_statistical import (
    compute_yearly_statistics,
    compute_overlap_band,
    generate_signals
)


def walk_forward_test(df, train_years, initial_capital):

    df = df.copy()

    df["Signal"] = 0

    df["Portfolio_Value"] = float(initial_capital)

    years = sorted(df["Year"].unique())

    capital = float(initial_capital)

    risk_fraction = 0.05  # risk 5% per trade

    total_trades = 0

    for i in range(train_years, len(years)):

        train_years_list = years[i-train_years:i]
        test_year = years[i]

        train_data = df[df["Year"].isin(train_years_list)]

        stats = compute_yearly_statistics(train_data)

        lower, upper = compute_overlap_band(stats)

        test_data = df[df["Year"] == test_year].copy()

        test_data = generate_signals(test_data, lower, upper)

        df.loc[test_data.index, "Signal"] = test_data["Signal"]

        trades_this_year = 0

        for idx, row in test_data.iterrows():

            signal = row["Signal"]

            if pd.isna(row["Return"]):

                df.loc[idx, "Portfolio_Value"] = capital
                continue

            if signal != 0:

                trades_this_year += 1
                total_trades += 1

                position = capital * risk_fraction

                capital += position * signal * row["Return"]

            df.loc[idx, "Portfolio_Value"] = capital

        print("Total trades:", trades_this_year)

    print("Final Portfolio Value:", capital)
    print("Total trades overall:", total_trades)

    return df
