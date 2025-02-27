import psycopg2
import logging
from psycopg2.extras import execute_values

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# This Class Handles DB connection, table creation, and data insertion
class Database:

    def __init__(self, dbname="pokemon_db", user="postgres", password="123456", host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = self.connect_db()

        self.create_table()

    # Establishes a connection to the PostgreSQL DB

        
        try:
            conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
            logging.info("Database connection successful")
            return conn
        
        except Exception as e:
            logging.error(f"Database connection failed: {e}")
            return None
    
    # Creates the Pokemon table if it does not exist
    def create_table(self):

        if not self.conn:
            logging.error("No database connection")
            return
        
        try:
            cur = self.conn.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS pokemon(id SERIAL PRIMARY KEY, name TEXT UNIQUE ,height INTEGER ,weight INTEGER,types TEXT,abilities TEXT);""")

            self.conn.commit()
            logging.info("Table created successfully")
            cur.close()

        except Exception as e:
            logging.error(f"Error creating table: {e}")
    
    # Inserts Pokemon data in bulk using execute_values for efficiency
    def insert_pokemon_batch(self, pokemon_list):

        if not self.conn:
            logging.error("No database connection")
            return
        
        try:
            cur = self.conn.cursor()
            query = """INSERT INTO pokemon (id, name, height, weight, types, abilities) VALUES %s ON CONFLICT (name) DO NOTHING"""

            values = [(p["id"], p["name"], p["height"], p["weight"], ', '.join(p["types"]), ', '.join(p["abilities"])) for p in pokemon_list]

            execute_values(cur, query, values)

            self.conn.commit()
            logging.info(f"Inserted {len(pokemon_list)} Pokémon successfully")
            cur.close()

        except Exception as e:
            logging.error(f"Error inserting Pokémon data: {e}")

    # Closes the DB connection
    def close_connection(self):

        if self.conn:
            self.conn.close()
            logging.info("Database connection closed")
