import psycopg2
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Database:

    # Initialize DB connection

    def __init__(self, dbname="apache_logs", user="postgres", password="123456", host="localhost", port="5432"):

        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = self.connect_db()

    # Establish connection to the PostgreSQL DB

    def connect_db(self):
        
        try:
            conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
            logging.info("Database connection successful")
            return conn
        
        except Exception as e:
            logging.error(f"Database connection failed: {e}")
            return None
        
    # Create Apache logs table if it does not exist

    def create_table(self):
       
        if not self.conn:
            logging.error("No database connection")
            return

        try:
            cur = self.conn.cursor()
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
            self.conn.commit()
            logging.info("Table created successfully")
            cur.close()

        except Exception as e:
            logging.error(f"Error creating table: {e}")

    # Insert parsed log data into the database

    def insert_logs(self, logs):
        
        if not self.conn:
            logging.error("No database connection")
            return

        try:
            cur = self.conn.cursor()
            query = """
                INSERT INTO apache_logs (ip, timestamp, method, url, status, os, browser, agent) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = [(log["ip"], log["timestamp"], log["method"], log["url"], log["status"], log["os"], log["browser"], log["agent"]) for log in logs]

            cur.executemany(query, data)
            self.conn.commit()
            logging.info(f"Inserted {len(logs)} logs successfully")
            cur.close()

        except Exception as e:
            logging.error(f"Error inserting data: {e}")

    # Close the DB connection

    def close_connection(self):
       
        if self.conn:
            self.conn.close()
            logging.info("Database connection closed")
