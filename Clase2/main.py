"""
Laboratorio III
Clase 2
Jeremias Riquero
"""
try:
    archivo1 = open('Prueba.txt', 'w', encoding='utf8')  # Creamos el archivo o lo buscamos con w, el utf8 es para
    # los caracteres especiales (acentos)
    archivo1.write('Creo mi Archivo txt en Python\nLas diferentes letras en la creación de un archivo y su uso\nr -> '
                   'es para leer un archivo\na -> para agregar más info\nx -> crear un archivo\nt -> especifica que '
                   'el archivo es de texto\nb -> especifica que el tipo de archivo es binario\nw+ | r+ -> leer y '
                   'escribir')  # Agregamos una linea al archivo
except Exception as e:
    print(e)
finally:
    archivo1.close()  # Cerramos el archivo para que se guarden los cambios hacemos un run file
