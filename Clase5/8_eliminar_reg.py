import psycopg2

# Eliminar registro

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            valores = (9,)
            cur.execute(sentencia, valores)
            registros_eliminados = cur.rowcount
            print(f'Registros ingresados: {registros_eliminados}')

except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
