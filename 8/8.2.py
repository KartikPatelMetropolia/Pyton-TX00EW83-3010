import mysql.connector

def get_airports(country_id):
    query = f"select name,type from airport where iso_country='{country_id}' order by type;"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for ans in result:
            print(f"The name of the airport is {ans[0]} and the type of the airport is {ans[1]}")
    return 0

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root_password',
         autocommit=True
         )

country_id = input("Enter the country code of the country:")
get_airports(country_id)