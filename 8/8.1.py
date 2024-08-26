import mysql.connector

def get_icao(icao):
    query = f"SELECT name,municipality from airport WHERE ident='{icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for ans in result:
            print(f"The name of the airport is {ans[0]} and the city name is {ans[1]}",end="")
    return 0

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Kartikpatel@1',
         autocommit=True
         )
icao = input("Enter the icao code of the airport to search:")
get_icao(icao)