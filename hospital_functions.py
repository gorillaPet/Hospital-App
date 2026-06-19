def get_hospital(conn, hospital_id):
    with conn.cursor() as cur:
        cur.execute(
        "SELECT * FROM hospital WHERE hospital_id = %s",
        (hospital_id,)
)
        return cur.fetchone()

