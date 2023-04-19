import configparser
import psycopg2
import json
from flask import Flask, request, jsonify

# Read the configuration file
config = configparser.ConfigParser()
config.read('settings.cfg')

# Get the database login information
host = config['database']['host']
port = config['database']['port']
database = config['database']['database']
user = config['database']['user']
password = config['database']['password']

flask_host = config['API']['host']
flask_port = config['API']['port']



def json_to_table(row_headers,json_data):
    
    table_html = '<table><tr>'
    for header in row_headers:
        table_html += '<th>{}</th>'.format(header)
    table_html += '</tr>'
    for data in json_data:
        table_html += '<tr>'
        for header in row_headers:
            table_html += '<td>{}</td>'.format(data[header])
        table_html += '</tr>'
    table_html += '</table>'

    return table_html

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = """
    <html>
    <head>
        <title>My Flask HTML Page</title>
    </head>
    <body>
        <h1>Hello!</h1>
        <br>
        <p>This is a the main page of the NBA pipeline project.</p>
        <br>        
        <p>Click <a href="/generalView">here</a> to go to the big table.</p>
        <br>
        <p>Click <a href="/query1">here</a> to go to the points per division</p>
        <br>
        <form action="/generalView" method="get">
            <label for="input_string">Input String:</label>
            <input type="text" id="input_string" name="input_string">
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """
    return html, 200, {'Content-Type': 'text/html'}


@app.route('/generalView',  methods=['GET'])
def get_widgets():
    input_string = request.args.get('input_string') 
    conn = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = conn.cursor()
    #cursor.execute("SELECT * FROM transformation_table WHERE column_name = %s", (input_string,))
    cursor.execute("SELECT * FROM transformation_table")

    row_headers = [desc[0] for desc in cursor.description] # Extract row headers

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()
    conn.close()

    return json_to_table(row_headers,json_data)


@app.route('/query1',  methods=['GET'])
def db_init():
    conn = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = conn.cursor()

    cursor.execute("SELECT team_division, MAX(pts_rank) as max_pts_rank FROM transformation_table GROUP BY team_division ORDER BY team_division DESC;")
    
    row_headers = [desc[0] for desc in cursor.description] # Extract row headers
    
    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))
    cursor.close()
    conn.close()

    return json_to_table(row_headers,json_data)

if __name__ == "__main__":
    app.run(host=flask_host, port=flask_port)