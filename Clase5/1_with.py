"""
Laboratorio III
Clase 5
Abel Pierna
Jeremias Riquero
"""
import psycopg2

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:  # Con esta sentencia no hace falta cerrar con un close al cursor
            sentencia = 'SELECT * FROM persona'
            cur.execute(sentencia)
            registros = cur.fetchall()
            print(registros)
except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
