import psycopg2

# Insertamos un registro

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Lucas', 'Salinas', 'lsalinas@gmail.com')
            cur.execute(sentencia, valores)
            registros_ingresados = cur.rowcount
            print(f'Registros ingresados: {registros_ingresados}')

except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
