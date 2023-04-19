from airflow import DAG
from airflow.models import Connection
from airflow import settings
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from dependencies.extraction.preProcessing import main as main_tables
from dependencies.extraction.extract import main as main_extraction
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
import subprocess
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

if 'database' not in config:
    raise ValueError('Missing [database] section in the configuration file')

# Connection parameters
conn_id = 'my_postgres_connection'
conn_type = 'postgres'

session = settings.Session()
existing_conn = session.query(Connection).filter(Connection.conn_id == conn_id).first()

if existing_conn:
    print(f"Connection '{conn_id}' already exists. Skipping creation...")
else:
    connection = Connection(
        conn_id=conn_id,
        conn_type=conn_type,
        host=database_host,
        login=database_user,
        password=database_password,
        schema=database_database,
        port=database_port
    )

    session.add(connection)
    session.commit()
    print(f"Connection '{conn_id}' created successfully!")

session.close()

# Python callables:

def _tables_preprocessing():
    main_tables()
    return

def _tables_extraction():
    main_extraction()
    return

def run_flask_app():
    subprocess.run(['python', 'dependencies/load/app.py'])

# DAG structure 

with DAG(
    dag_id='first_sample_dag',
    start_date=datetime(2022, 5, 28),
    schedule_interval=None) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    db_ingestion = PythonOperator(
        task_id="database_ingestion",
        python_callable= _tables_preprocessing
    )

    db_extraction = PythonOperator(
        task_id="extracting_data",
        python_callable= _tables_extraction
    )

    db_transform = PostgresOperator(
        task_id='postgres_transform_data',
        postgres_conn_id='my_postgres_connection',
        sql='dependencies/transformation/sql/join_transform.sql'
    )

    flask_container = PythonOperator(
        task_id='flask_container_build',
        python_callable=run_flask_app,
    )

    end_task = EmptyOperator(
        task_id='end'
    )

start_task >> db_ingestion
db_ingestion >> db_extraction
db_extraction >> db_transform
db_transform >> flask_container
flask_container >> end_task