"""
Laboratorio III
Clase 1
Jeremias Riquero
"""
from Clase1.BusquedaException import BusquedaException
# Forma base
resultado = None
a = 0  # Las variables se puede iniciar dentro o fuera del try
try:
    b = 10  # Como también dentro
    resultado = b / a
except Exception as ex:  # Generalmente se trata de ser genérico y por eso se suele usar Exception pero también sé
    # puede ser más específico
    print(f'Aquí hay un error: {ex}')
print(f'Resultado: {resultado}')
print('sigue el código...')

# Usamos input, Exceptions especificas, else y finally
resultado2 = None
try:
    a = int(input('Ingrese un número: '))
    b = int(input('Ingrese otro número: '))  # Podemos usar input dentro de estas expresiones
    resultado2 = a / b
    # Esta es la forma para ser más específico, primero se pone la clase más específica y después el Exception,
    # si no entra en una entra en la otra
except ZeroDivisionError as problemaEspecifico:
    print(f'Aquí hay un error especifico ZeroDivisionError: {problemaEspecifico}')
except Exception as problema:
    print(f'Aquí hay un error: {problema}')
else:  # Usamos else para que nos lance un mensaje, etc. en el caso de que no hayan Exceptions
    print('El programa no tiene ningún error')
finally:  # El finally es un bloque siempre se va reproducir al final haya o no una Exceptions
    print('La revisión a finalizado')
print(f'Resultado: {resultado2}')
print('sigue el código')

# Exception Personalizado

num = None
try:
    num = int(input('Ingrese un número: '))
    if num == 0:
        raise BusquedaException('Error, el número ingresado es menor a 0')

except Exception as problem:
    print(f'Error encontrado: {type(problem)}')
