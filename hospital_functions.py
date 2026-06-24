
#Returns hospital based on h_id
def get_hospital(conn, hospital_id):
    with conn.cursor() as cur:
        cur.execute(
        "SELECT * FROM hospital WHERE hospital_id = %s",
        (hospital_id,)
)
        return cur.fetchone()


# Test function to return all hospitals
def list_hospitals(conn):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM hospital"
)

        return cur.fetchall()
    

# Uses the hd table to match h_id and returns hospitals with that department   
def find_department(conn, dept_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT h.*
            FROM hospital h
            JOIN hospital_department hd
                ON h.hospital_id = hd.hospital_id
            WHERE hd.department_id = %s
            """,
            (dept_id,)
        )

        return cur.fetchall()
