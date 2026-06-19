import psycopg
import os
from dotenv import load_dotenv
from hospital_functions import *

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

hospital_id = 2

hospital = get_hospital(conn, hospital_id)

conn.close()

print(hospital)

