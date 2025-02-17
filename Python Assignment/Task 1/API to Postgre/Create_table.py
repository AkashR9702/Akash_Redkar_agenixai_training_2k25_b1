from Database_conn import connect_db

def Create_table():

    conn = connect_db()
    if not conn:
        print("Database connection failed!")
        return

    cur = conn.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS pokemon(id SERIAL PRIMARY KEY, name TEXT UNIQUE ,height INTEGER ,weight INTEGER,types TEXT,abilities TEXT);""")
    conn.commit()
    print("Table Created Succesfully")

    cur.close()
    conn.close()

if __name__ == "__main__":
    Create_table()