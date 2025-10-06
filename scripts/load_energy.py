from db_config import get_engine

def load_data(df, table_name="energy_consumption"):
    print(f"🔹 Loading data to table `{table_name}`...")
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print("✅ Data loaded successfully!")
