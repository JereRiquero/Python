"""
Laboratorio III
Clase 4
Jeremias Riquero
"""
import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
cursor = connection.cursor()
sentencia = 'SELECT * FROM persona '
cursor.execute(sentencia)
registro = cursor.fetchall()
for row in registro:
    print(row)
cursor.close()
connection.close()
