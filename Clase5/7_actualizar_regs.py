import psycopg2

# actualizar varios registros

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = (
                ('Jeremias', 'Riquero', 'jriquero@gmail.com', 2),
                ('Matias', 'Pierna', 'mpierna3@gmail.com',1)
            )
            cur.executemany(sentencia, valores)
            registros_actualizados = cur.rowcount
            print(f'Registros ingresados: {registros_actualizados}')

except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
