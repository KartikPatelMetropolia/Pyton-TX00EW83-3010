import mysql.connector
import geopy
from geopy.distance import geodesic

connection = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='root',
                password='root_password',
                autocommit=True
    )

def get_corrdinates(icao):
    query = f"Select latitude_deg,longitude_deg from airport where ident='{icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def get_name(icao):
    query = f"select name from airport where ident='{icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    name = str(result[0])
    return name

first = input("Enter the icao code of the first airport:")
second = input("Enter the icao code of the second airport:")
name1 = get_name(first)
name2 = get_name(second)
cordinates1 = get_corrdinates(first)
cordinates2 = get_corrdinates(second)

print(f"The distance between {name1} and {name2} is {geodesic(cordinates1,cordinates2).km:.2f} km")