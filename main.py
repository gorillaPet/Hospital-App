import psycopg
import os
from dotenv import load_dotenv
from hospital_functions import *
from card_print import *

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

hospital_id = input("Which hospital ID?: ")

if hospital_id == "00":
    hospitals = list_hospitals(conn)
    for hospital in hospitals:
        print(hospital)

else:
    hospital = get_hospital(conn, hospital_id)
    print(hospital)

conn.close()



