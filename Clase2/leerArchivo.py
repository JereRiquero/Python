archivo1 = open('Prueba.txt', 'r', encoding='utf-8')
#  print(archivo1.read())  # Para leer el archivo en la terminal
#  print(archivo1.read(20))  # Muestra la cantidad de caracteres indicados en los paréntesis
#  print(archivo1.readline())  # Nos lee la línea entera

#  ITERAR CON CICLO FOR
# for linea in archivo1:
# print(linea)
# print(archivo1.readlines())  # Lo convertimos en una lista
# print(archivo1.readlines()[3])  # Llamamos a una linea en larticular
archivo2 = open('Copia.txt', 'a', encoding='utf-8')  # creamos un segundo archivo y con él a de append copiamos la
# info de archivo1
archivo2.write(archivo1.read())  # Aquí es donde se copia lo de archivo1 en archivo2
archivo1.close()  # cerramos los archivos
archivo2.close()
# siempre que hagamos run nos va a copiar la info de archivo1 en archivo2 repetidas veces
