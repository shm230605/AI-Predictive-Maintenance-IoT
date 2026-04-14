import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # Remove missing values
    df = df.dropna()
    return df