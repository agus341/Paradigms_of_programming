### Ejercicio 17: Herencia - Clase Vehiculo
#
# Imagina que estás desarrollando un sistema para una empresa de transporte. 
# Debes modelar diferentes tipos de vehículos usando clases en Python.
#
# Crea una clase base llamada Vehiculo que tenga: marca y modelo,
# y un método informacion() que imprima la marca y el modelo.
# Crea una clase derivada llamada Auto que herede de Vehiculo y además tenga:
# num_puertas y un método informacion() que además de la marca y el modelo, 
# imprima el número de puertas.
# Crea otra clase derivada llamada Moto que herede de Vehiculo y además tenga:
# cilindrada y un método informacion() que además de la marca y el modelo, imprima la cilindrada.
# Crea un objeto de tipo Auto y otro de tipo Moto, y llama a su método informacion()


class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def informacion(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo}", end = "\n")

class Auto(Vehiculo):
    def __init__(self,marca,modelo,num_puertas):
        super().__init__(marca,modelo)
        self.num_puertas = num_puertas
    
    def informacion(self):
        super().informacion()
        print(self.num_puertas)

class Moto(Vehiculo):
    def __init__(self,marca,modelo,cilindrada):
        super().__init__(marca,modelo)
        self.cilindrada = cilindrada

    
    def informacion(self):
        super().informacion()
        print(self.cilindrada)


auto = Auto("Ford","Focus",3)
moto = Moto("Benelli","...",250)

auto.informacion()
moto.informacion()

a = auto.informacion
print(type(a))
a()

        