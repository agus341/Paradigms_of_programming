from random import randint 
#  columna --> año
#  fila --> sucursal
# años --> M entre [1,2]
# sucursales --> N entre [1,2]

def generar_matriz():
    # columnas de 0 a 29, y filas de 0 a 34. 
    # Para accederlas según el enunciado sumarle una unidad a los índices
    matriz_monto = [[randint(0,1000) for _ in range(2)] for _ in range(2)]
    return matriz_monto

def sucursal_masventas(matriz):
    ventas = []
    # n itera las sucursales
    for n in range(2):
        cont = 0
        # m recorre los años para cada sucursal
        for m in range(2):
            cont += matriz[n][m]
        # El índice de ventas se corresponde con el número de sucursal (su correspondiente venta)
        ventas.append(cont)
    
    max_ventas = max(ventas)

    for i in range(2):
        if ventas[i] == max_ventas:
            return i
        

a = generar_matriz()
print(f"la sucursal que más vendió en los 2 años fue {1+(sucursal_masventas(a))}")
for i in range(2):
    print(a[i])

    