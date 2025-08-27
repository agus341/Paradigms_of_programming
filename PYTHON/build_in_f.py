#son funciones que vienen ya definidas en python

lista = [1,2,3,4,5,4,3,2,1]
#map aplica la función al iterable
print(list(map(lambda x: x*2, lista)))
print(list(filter(lambda x: x % 2 == 0, lista)))
from functools import reduce

# Reduce toma un iterable y le aplica una función a sus elementos para devolver un solo valor.
# Por ejemplo, sumar los elementos de una lista
print(reduce(lambda x,y: x + y, lista))

# Zip genera un iterable de tuplas que contienen los elementos i-esímos de los iterables pasados por parámetro.
print(list(zip('abcdefg', range(3), range(4))))

# Sorted oredena de menor a mayor por defecto. 
print(sorted(lista, key = lambda x: x % 2 ))