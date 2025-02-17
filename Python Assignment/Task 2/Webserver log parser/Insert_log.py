from Database_conn import connect_db

def insert_logs(logs):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            query = """
                INSERT INTO apache_logs (ip, timestamp, method, url, status, os, browser, agent) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = [(log["ip"], log["timestamp"], log["method"], log["url"], log["status"], log["os"], log["browser"], log["agent"]) for log in logs]

            cur.executemany(query, data)  
            conn.commit()
            print(f"Inserted  logs into the database successfully")

            cur.close()
        except Exception as e:
            print("Error inserting data", e)
        finally:
            conn.close()

if __name__ == "__main__":
    from Parse_log import parse_log_file

    logs = parse_log_file()
    insert_logs(logs)



