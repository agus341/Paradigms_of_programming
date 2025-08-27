# Ejercicio Práctico : Calculadora de divisiones
#
# Crea un programa en Python que reciba una lista de pares de números
# (dividendo y divisor) e intente realizar la división de cada par
# 
# El programa debe manejar los siguientes casos utilizando bloques try y except:
# Si el divisor es cero, debe mostrar un mensaje de error: "Error: No se puede
# dividir por cero"
# Si alguno de los valores no es un número válido (por ejemplo, una letra), debe 
# mostrar:
# "Error: Entrada inválida. Ambos valores deben ser números."
# Si la división es exitosa, debe imprimir el resultado en el formato: 
# "Resultado de dividir X entre Y es Z"

#Verificación del n
while True:
    try:
        n = int(input("Ingresar cantidad de pares de numeros."))
    except ValueError:
        print("Error: Entrada inválida. Debe ingresar un numero entero.")
        continue
    else:
        if n <= 0:
            print("Error: Debes ingresar un número entero positivo.")
        else:
            break    


lista_pares = []

for i in range(n):
    while True:
        try:
            dividendo = int(input("Ingrese dividendo: "))
            divisor = int(input("Ingrese divisor: "))
            z = dividendo / divisor
        except ValueError:
            print("Error: Algún valor no entero fue ingresado.")
        except ZeroDivisionError:
            print("Error: se produjo una división por cero")
        else:
            z = round(z,2)
            a = [dividendo,divisor,z]
            lista_pares.append(a)
            break

for i in range(n):
    print(lista_pares[i])
       


    
