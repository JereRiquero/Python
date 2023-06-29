import psycopg2

# actualizar un registro

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = ('Lucia', 'Castilla', 'lcastilla@gmail.com', 9)
            cur.execute(sentencia, valores)
            registros_actualizados = cur.rowcount
            print(f'Registros ingresados: {registros_actualizados}')

except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
