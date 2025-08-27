# Programa para sumar dos matrices de enteros de tamaño n x m
# y mostrar el resultado en pantalla.
# Se asume que las matrices son de enteros y del mismo tamaño.

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# En el for interno se recorre las columnas de las matrices, el for externo recorre las filas.
# Recordar que matriz1[0] --> [1, 2, 3] entonces len(matriz1[0]) --> 3 , numero de columnas
# Notar que matriz1 --> [[1, 2, 3], [4, 5, 6], [7, 8, 9]] entonces len(matriz1) devuelve la cantidad de elementos (listas en este caso)
# representando la cantidad de filas. Se puede decir que matriz1 es una lista de listas, la forma de usar matrices en python

matriz_suma = [[matriz1[i][j]+matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]


for i in range(len(matriz_suma)):
    print(matriz_suma[i])