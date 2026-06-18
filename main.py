import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnectionError(Exception):
    pass

try: 
    conn = psycopg.connect(

        host="localhost",
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    print("Connected to DB...")



except psycopg.OperationalError as e:
    raise DatabaseConnectionError("Failed to connect... ") from e

with conn.cursor() as cur:
    cur.execute("SELECT version();")
    print(cur.fetchone())

conn.close()

