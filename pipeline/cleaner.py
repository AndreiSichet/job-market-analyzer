import pandas as pd
def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    # Fill missing values
    df["location"] = df["location"].fillna("Remote")
    # Normalize text
    df["title"] = df["title"].str.lower()
    df["company"] = df["company"].str.lower()
    return df