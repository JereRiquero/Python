from Clase3.domino.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('\nOpciones: ')
        print('1. Agregar Películas')
        print('2. Listar las películas')
        print('3. Eliminar catálogo de películas')
        print('4. Salir')
        opcion = int(input('Digite una opción de menú (1-4):\n-> '))
        if opcion == 1:
            nombre_pelicula = input('Digité el nombre de la película:\n-> ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error de tipo {e}')
        opcion = None
    else:
        print('Salimos del programa...')
