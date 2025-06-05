# #Crear una lista con números aleatorios y contar el número de repeticiones de cada número.
# Imprimir un menu con las opciones: 
# 1. Crear una nueva lista con número enteros aleatorios seleccionando la cantidad de numeros y entre 0 y cual hacerlo  
# 2. Imprimir la lista creada, sino está creada mandar un mensaje de aviso 
# 3. Mostrar las repeticiones de cada elemento 
# 4. Mostrar los porcentajes de repeticion  
# 5. Generar una lista nueva sin los elementos repetidos 
# 6 Salir

import random

def contar_repetidos(lista):
    """Cuenta las repeticiones de cada elemento en la lista."""
    repeticiones = {}
    for num in lista:
        if num in repeticiones:
            repeticiones[num] += 1
        else:
            repeticiones[num] = 1
    return repeticiones

def mostrar_porcentajes(repeticiones, total):
    """Muestra los porcentajes de repetición de cada elemento."""
    for num, count in repeticiones.items():
        dic = {}
        porcentaje = (count / total) * 100
        dic[num] = porcentaje
        print(f"El número {num} se repite {count} veces ({porcentaje:.2f}%)")
    
def lista_sin_repetidos(lista):
    """Genera una lista nueva sin los elementos repetidos."""
    return list(set(lista))





num_max = int(input("Ingrese el número máximo: "))
cant_aleat = int(input("Ingrese la cantidad de números aleatorios:"))

lista = [random.randint(1,num_max) for _ in range(cant_aleat)]




if __name__ == "__main__":

