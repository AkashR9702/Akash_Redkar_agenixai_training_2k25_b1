from Create_table import create_table
from Parse_log import parse_log_file
from Insert_log import insert_logs

def main():
   
    print("Creating table...")
    create_table()

    print("Parsing log file...")
    logs = parse_log_file()

    print("Inserting parsed logs into the database...")
    insert_logs(logs)

if __name__ == "__main__":
    main()
