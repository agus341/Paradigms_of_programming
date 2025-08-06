
#funciones de orden superior: tiene que recibir funciones como parametro o devolver fuciones
"""
def suma_uno(x):
    return x+1

def suma_dos(x):
    return x+2

def suma_nros_mas_otro(a,b, f_suma):
    return f_suma(a+b)

print(suma_nros_mas_otro(3,4,suma_uno))
print(suma_nros_mas_otro(3,4,suma_dos))
"""

#ejercicio 4: Aplica una función
 # escribe una función que reciba otra función y un número
 # y retorne el resultado de aplicar esa función al número

f = lambda x: x+1
f1 = lambda x: x-1
f2 = lambda x: x**2

def oreden_sup(c,g):
    return g(c)

print(oreden_sup(1,f))
print(oreden_sup(1,f1))
print(oreden_sup(1,f2))