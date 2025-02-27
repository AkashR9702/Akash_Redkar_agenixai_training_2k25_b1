from Database import Database
from LogParser import LogParser
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Starting log processing...")
    
    # Initialize DB and create table
    db = Database()
    db.create_table()
    
    # Parse logs
    parser = LogParser()
    logs = parser.parse_log_file()
    
    if logs:

        # Insert parsed logs into the DB
        db.insert_logs(logs)        
        logging.info("Log data inserted successfully.")
    else:
        logging.warning("No logs found to insert.")
    
    # Close DB
    db.close_connection()            
    logging.info("Processing complete.")

if __name__ == "__main__":
    main()

