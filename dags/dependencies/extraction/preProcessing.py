import psycopg2
from dependencies.extraction.sqlQueries import create_table_queries, drop_table_queries, tableNames
from dependencies.database import DatabaseConnector

# def create_database():
#     """
#     - Creates and connects to the nbadb
#     - Returns the connection and cursor to nbadb
#     """

#     conn = psycopg2.connect(database='nbadb',
#                         user='example_user',
#                         password='example_password', 
#                         host='datasource', port='5432')
  

#     conn.autocommit = True
#     cur = conn.cursor()
    
#     return cur, conn





def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(e.message)

def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(e.message)

def insert_tables(cur,conn,tableName):
    fileName = '/opt/airflow/dags/dependencies/extraction/csv/' + tableName + '.csv'
    with open(fileName, 'r') as f:
        next(f) # Skip the header.
        cur.copy_from(f, tableName, sep=',')
    conn.commit()


def main():
    """
    - Drops (if exists) and Creates the nbadb database. 
    
    - Establishes connection with the nbadb database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """

    # Create an instance of DatabaseConnector 
    db_connector = DatabaseConnector()

    # Get the cursor and connection objects
    cur, conn = db_connector.get_cursor_and_connection()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    for table in tableNames:
        insert_tables(cur,conn,table)

    
    conn.close()


if __name__ == "__main__":
    main()