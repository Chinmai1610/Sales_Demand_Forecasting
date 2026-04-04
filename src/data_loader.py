import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    return df

def preprocess_data(df):
    # Ensure no missing values for the model
    df = df.fillna(method='ffill').fillna(method='bfill')
    return df