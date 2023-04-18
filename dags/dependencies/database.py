import psycopg2

class DatabaseConnector:
    _instance = None

    def __new__(cls, database='nbadb', user='example_user', password='example_password', host='172.18.0.2', port='5432'):
        """
        Singleton pattern implementation to ensure only one instance of DatabaseConnector is created
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = psycopg2.connect(database=database,
                                                  user=user,
                                                  password=password,
                                                  host=host,
                                                  port=port)
            cls._instance.conn.autocommit = True
            cls._instance.cur = cls._instance.conn.cursor()
        return cls._instance

    def get_cursor_and_connection(self):
        """
        Returns the cursor and connection objects
        """
        return self.cur, self.conn