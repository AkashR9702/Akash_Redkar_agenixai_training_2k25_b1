import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(dbname ="pokemon_db", user ="postgres", password ="123456",host="localhost", port = "5432")

        return conn
    except Exception as e:
        print("Connection Failed",e)

        return None