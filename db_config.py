import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "15904")
DB_NAME = os.getenv("DB_NAME")

# Debugging print
print("🔍 ENV CHECK:")
print("DB_HOST =", DB_HOST)
print("DB_PORT =", DB_PORT)
print("DB_USER =", DB_USER)
print("DB_NAME =", DB_NAME)

def get_engine():
    if not all([DB_USER, DB_PASS, DB_HOST, DB_NAME]):
        raise ValueError("❌ Missing one or more DB environment variables. Check your .env or Codespaces Secrets.")
    url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    return create_engine(url)
