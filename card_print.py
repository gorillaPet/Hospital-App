#takes connection, dept_id, hospital and prints the relevant details. 

def print_card(conn, dept_id, hospital: tuple):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM department WHERE department_id = %s", #change this to capability once that table is made. 
                    (dept_id,))

        dept_name = cur.fetchone()


    print(hospital[1])   
    print(hospital[3]) 