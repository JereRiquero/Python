import psycopg2

# LLamamos a varios registro de forma dinámica con input

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = input('Digite los números de las columnas que desea ver (separado por coma): ')
            llaves_primaria = (tuple(entrada.split(',')),)
            cur.execute(sentencia, llaves_primaria)
            registros = cur.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
