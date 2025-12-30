from scripts_dbt.extract_energy import extract_data
from scripts_dbt.load_energy import load_data
import subprocess
import os

DBT_PROJECT_DIR = os.path.join(os.getcwd(), "dbt_energy")

if __name__ == "__main__":
    print("🚀 Starting ELT pipeline...")

    # 1. Extract
    df_raw = extract_data()

    # 2. Load RAW
    load_data(df_raw)

    # 3. Transform with dbt
    print("🔹 Running dbt transformations...")
    subprocess.run(
        ["dbt", "run"],
        cwd=DBT_PROJECT_DIR,
        check=True
    )
    subprocess.run(
        ["dbt", "test"],
        cwd=DBT_PROJECT_DIR,
        check=True
    )

    print("✅ ELT pipeline completed successfully!")
