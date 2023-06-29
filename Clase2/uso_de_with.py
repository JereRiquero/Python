# usamos with par a trabajar de forma más sencilla con los archivos, ya que los abre y cierra automáticamente sin
# necesidad de que lo hagamos nosotros, usando __enter__ y __exit__

# with open('Prueba.txt', 'r', encoding= 'utf-8') as archivo:
#    print(archivo.read())
from Clase2.MetodoAutomatico import MetodoAutomatico

with MetodoAutomatico('Prueba.txt') as archivo:  # De esta formo podemos ver como actua el __enter__ y el __exit
    print(archivo.read())
