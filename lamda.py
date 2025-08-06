"""
def suma(a,b):
    return a+b

c = suma(1,2)
print(c)


c = lambda a,b : a + b

print(c(1,2))

#funciones rápidas y simples en una sola línea.
#No recomendable para funciones largas.
cuadrado = lambda x: x**2

concatenar = lambda t,h: t + h
s = concatenar("agustín ","Jesús")

#funciones anidadas
def sumar3(c):
    return lambda a,b : a + b + c

a = sumar3(3)
t = a(3,2)
print(t)
print(sumar3(3)(3,2))
"""

#funcion lambda que me devuelva un string al revés
invertir = lambda s : s[::-1]
print(invertir("hola"))

#función lambda que me diga si es palíndromo

es_palindromo = lambda s: s == s[::-1]
print(es_palindromo("neuquen"))
print(es_palindromo("hola"))