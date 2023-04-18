from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from dependencies.extraction.preProcessing import main as main_tables
from dependencies.extraction.extract import main as main_extraction
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
import subprocess


def _tables_preprocessing():
    main_tables()
    return

def _tables_extraction():
    main_extraction()
    return

def run_flask_app():
    # Use subprocess to call the Flask application's app.py file
    subprocess.run(['python', 'dependencies/load/app.py'])



# Print PostgreSQL details
# print("PostgreSQL server information")
# print(conn.get_dsn_parameters(), "\n")
# # Executing a SQL query
# cur.execute("SELECT version();")
# # Fetch result
# record = cur.fetchone()
# print("You are connected to - ", record, "\n")
# print("-------------- \n")


with DAG(
    dag_id='first_sample_dag',
    start_date=datetime(2022, 5, 28),
    schedule_interval=None
) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    print_hello_world = BashOperator(
        task_id='print_hello_world',
        bash_command='pwd'
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

start_task >> print_hello_world
print_hello_world >> db_ingestion
db_ingestion >> db_extraction
db_extraction >> db_transform
db_transform >> flask_container
flask_container >> end_task