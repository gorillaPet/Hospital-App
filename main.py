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

quit_app = False

#Main loop
while not quit_app:

    for i in range(25):
        print("*", end="")
        
    print("\nWhich department ID?: ")
    dept_id = input("Neuro: 1\n"  "Cardiac: 2\n" "Trauma: 3\n\nSelection: ")

    if dept_id == "quit":
        quit_app = True
        break

    elif dept_id == "00":
        hospitals = list_hospitals(conn)
        for hospital in hospitals:
            print(hospital)

    else:
        hospitals = find_department(conn, dept_id)
        for hospital in hospitals:
            print(hospital)

conn.close()


