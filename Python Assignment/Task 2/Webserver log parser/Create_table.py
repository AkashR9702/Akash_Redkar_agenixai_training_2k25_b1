from Database_conn import connect_db

def create_table():
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS apache_logs (
                    id SERIAL PRIMARY KEY,
                    ip VARCHAR(50),
                    timestamp TIMESTAMP,
                    method VARCHAR(10),
                    url TEXT,
                    status INTEGER,
                    os VARCHAR(50),
                    browser VARCHAR(50),
                    agent TEXT
                );
            """)
            conn.commit()
            print("Table created successfully.")

        except Exception as e:
            print("Error creating table:", e)

        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    create_table()

