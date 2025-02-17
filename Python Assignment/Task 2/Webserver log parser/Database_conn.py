import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(dbname="apache_logs",user="postgres", password= "123456", host="localhost", port="5432")
        return conn

    except Exception as e:
        print("Database connnection Failed",e)
