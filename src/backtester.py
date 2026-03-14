import pandas as pd

def backtest_strategy(df, initial_capital: int):

    cash = initial_capital
    position = 0
    portfolio_values = []

    for i in range(len(df)):

        price = df["Close"].iloc[i]
        signal = df["Signal"].iloc[i]

        # BUY
        if signal == 1 and cash > 0:
            position = cash / price
            cash = 0
            print(f"BUY at {price:.2f}")

        # SELL
        elif signal == -1 and position > 0:
            cash = position * price
            position = 0
            print(f"SELL at {price:.2f}")

        portfolio_value = cash + position * price
        portfolio_values.append(portfolio_value)

    df["Portfolio_Value"] = portfolio_values

    final_value = portfolio_values[-1]

    return df, final_value
