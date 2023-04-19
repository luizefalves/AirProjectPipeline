import psycopg2
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('/opt/airflow/dags/settings.cfg')

# Get the database login information
database_host = config.get('database', 'host')
database_port = config.getint('database', 'port')
database_database = config.get('database', 'database')
database_user = config.get('database', 'user')
database_password = config.get('database', 'password')


class DatabaseConnector:
    _instance = None

    def __new__(cls, database=database_database, user=database_user, password=database_password, host=database_host, port=database_port):
        """
        Singleton  implementation to ensure only one instance of DatabaseConnector is created
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