import psycopg2

# LLamamos a un registro

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # Placeholder
            id_persona = 2
            cur.execute(sentencia, (id_persona,))
            registros = cur.fetchone()
            print(registros)
except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
