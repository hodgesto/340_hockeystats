from flask import Flask, render_template
from db_connector.db_connector import connect_to_database, execute_query

app = Flask(__name__)

@app.route('/teams')
def teams():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * from teams;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           navbar=render_template("layouts/navbar.html"),
                           body=render_template("team.html", rows=result))

@app.route('/')
def index():
    return "<i>Are you looking for /db-test or /hello ?</i>"

@app.route('/db-test')
def test_database_connection():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * from teams;"
    result = execute_query(db_connection, query)
    return render_template('db_test.html', rows=result)

@app.route('/scheudle')
def display_schedule():
    print("Querying database for teams and games")
    db_connection = connect_to_database()
    query = "SELECT teamName FROM teams RIGHT JOIN games GROUP BY gameTime;"
    result = execute_query(db_connection, query)
    return render_template('db_test.html', rows=result)
