
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

# ejercicio 5: Función de composición
# Implementa una función que reciba dos funciones y devuelva
# una nueva función que sea la composición de ambas

f = lambda x: x+1
g = lambda x: x*3

def compuesta(f,g):
    return lambda x: f(g(x))

a = compuesta(f,g)
print(a(1))


### ejercicio 7: clase con __str___
#  Crear una clase libro  con atributos título y autor
#  Redefine el método __str__ para que al imprimir un objeto
#  Muestre título y autor

# Método rústico
class Libro:
    titulo = ""
    autor = ""

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    

libro1 = Libro()
libro1.titulo = "Hola"
libro1.autor = "Agus"

libro2 = Libro()
libro2.titulo = "Chau"
libro2.autor = "Agus2"

print(libro1)
print(libro2)

class Libro1:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
libro1 = Libro1("hola","Agus")

libro2 = Libro1("chau","agus2")

print(libro1)
print(libro2)