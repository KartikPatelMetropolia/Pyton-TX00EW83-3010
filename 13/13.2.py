from flask import Flask, Response
import json
import mysql.connector

connection = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='root',
                password='Kartikpatel@1',
                autocommit=True
    )

app = Flask(__name__)
@app.route('/airport/<airport_ident>')
def send_name(airport_ident):
    query = f"select ident,name,municipality from airport where airport.ident='{airport_ident}';"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    response = {
        "ICAO" : result[0],
        "Name" : result[1],
        "Location" : result[2]
    }
    return response
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)