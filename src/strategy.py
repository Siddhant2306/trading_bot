def compute_statistics(df, window=60):
 
    df["Return"] = df["Close"].pct_change()

    # Rolling statistics
    df["Rolling_Mean"] = df["Return"].rolling(window=window).mean()
    df["Rolling_STD"] = df["Return"].rolling(window=window).std()

    # Z-score
    df["Z_Score"] = ((df["Return"]) - df["Rolling_Mean"] / df["Rolling_STD"])

    return df


def generate_signals(df):

    df["Signal"] = 0

    df.loc[df["Z_Score"] < -2, "Signal"] = 1   
    df.loc[df["Z_Score"] > 2, "Signal"] = -1   

    return df
