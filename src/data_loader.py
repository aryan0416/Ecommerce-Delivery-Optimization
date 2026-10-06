import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'], errors='coerce')
    return df
