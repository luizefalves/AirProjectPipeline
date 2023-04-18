import psycopg2
import os
from psycopg2 import Error
from dependencies.database import DatabaseConnector

def read_sql(cur,conn):
    files = os.listdir('/opt/airflow/dags/dependencies/extraction/sql/')
    for file in files:
        filename = f'/opt/airflow/dags/dependencies/extraction/sql/{file}'
        with open(filename, 'r') as f:
            sql_query = f.read()
        cur.execute(sql_query)
    # Commit the changes to the database and close the cur and conn
    conn.commit()



def main():
    try:
        # Create an instance of DatabaseConnector 
        db_connector = DatabaseConnector()

        # Get the cursor and connection objects
        cur, conn = db_connector.get_cursor_and_connection()

        read_sql(cur, conn)

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (conn):
            cur.close()
            conn.close()
            print("PostgreSQL conn is closed")

if __name__ == "__main__":
    main()