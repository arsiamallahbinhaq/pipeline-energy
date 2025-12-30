from sqlalchemy import text
from db_config import get_engine

def load_data(df, table_name="raw_energy"):
    print("🔹 Loading data to raw schema...")
    engine = get_engine()

    with engine.begin() as conn:
        # 1️⃣ truncate table
        conn.execute(text(f"TRUNCATE TABLE raw.{table_name}"))

        # 2️⃣ insert data
        df.to_sql(
            table_name,
            conn,
            schema="raw",
            if_exists="append",
            index=False
        )

    print("✅ Data refreshed in raw.raw_energy")

