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

    dept_id = input("""
Departments 
-----------
                                       
1: Neuro
2: Trauma
3: Cardiac
                    
Selection: """
                    )

    if dept_id == "quit":
        quit_app = True
        break

    elif dept_id == "00":
        hospitals = list_hospitals(conn)
        for hospital in hospitals:
            print_card(conn, dept_id, hospital)

    else:
        hospitals = find_department(conn, dept_id)
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM department WHERE department_id = %s", (dept_id,)
            )
            dept = cur.fetchone()

        ############################## Delete after GUI implementation OR keep for debug ################################
        
        
        print(f"""
              
--------------------
              {dept[1]}
--------------------
""")
        


        for hospital in hospitals:
            print_card(conn, dept_id, hospital)
            print("")

conn.close()


