import pandas as pd
import os

def extract_data():
    url = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    print("🔹 Extracting data from OWID...")
    df = pd.read_csv(url)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_energy.csv", index=False)
    return df
