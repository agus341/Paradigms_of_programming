#el método abstracto es obligatorio para todas las clases hijas.
#una clase con método abstracto no puede generar objetos

### Ejercicio 21 : Polimorfismo - Clase Figuras Geométricas

# Crea un programa que permita calcular el área de diferentes figuras geométricas 
# utilizando polimorfismo.
#
# 1. Define una clase abstracta llamada 'Figura' con un método abstracto 'calcular_area()'.
# 2. Crea al menos dos clases que hereden de 'Figura': 'Circulo' y 'Rectangulo'.
#    - 'Circulo' debe tener un atributo 'radio'.
#    - 'Rectangulo' debe tener atributos 'base' y 'altura'.
# 3. Implementa el método 'calcular_area()' en cada subclase para calcular el área apropiada.
# 4. Escribe una función 'mostrar_areas(figuras)' que reciba una lista de figuras y, usando polimorfismo, imprima el área de cada una.

from abc import ABC,abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

class Rectangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


def mostrar_areas(figuras):
    for figura in figuras:
        print(figura.calcular_area())

figuras = [Circulo(4),Rectangulo(2,2)]

mostrar_areas(figuras)
 

