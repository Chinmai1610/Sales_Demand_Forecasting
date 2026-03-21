import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    df = df.dropna()
    return df