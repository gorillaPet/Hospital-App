def get_hospital(conn, hospital_id):
    with conn.cursor() as cur:
        cur.execute(
        "SELECT * FROM hospital WHERE hospital_id = %s",
        (hospital_id,)
)
        return cur.fetchone()



def list_hospitals(conn):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM hospital"
)

        return cur.fetchall()