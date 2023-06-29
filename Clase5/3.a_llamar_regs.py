import psycopg2

# LLamamos a varios registros

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:
            # sentencia = 'SELECT * FROM persona WHERE id_persona IN (1, 2)'
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s ORDER BY id_persona ASC'
            id_persona = range(1, 100)
            # cur.execute(sentencia)
            cur.execute(sentencia, (tuple(id_persona),))
            registros = cur.fetchall()
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
