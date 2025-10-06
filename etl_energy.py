from scripts.extract_energy import extract_data
from scripts.transform_energy import transform_data
from scripts.load_energy import load_data

if __name__ == "__main__":
    print("🚀 Starting ETL pipeline...")
    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    load_data(df_clean)
    print("✅ ETL pipeline completed successfully!")
