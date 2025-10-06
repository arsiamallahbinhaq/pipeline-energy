import pandas as pd

def transform_data(df):
    print("🔹 Transforming data...")
    df = df[["country", "year", "primary_energy_consumption", "population", "gdp"]]
    df = df.dropna(subset=["primary_energy_consumption"])
    df = df[df["year"] >= 2000]
    df["primary_energy_consumption"] = df["primary_energy_consumption"].round(2)
    df.to_csv("data/clean_energy.csv", index=False)
    return df
