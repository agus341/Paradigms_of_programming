class Animal():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def hablar(self):
        pass

class Perro(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
    def hablar(self):
        print("¡Guauuu!")

class Gato(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
    def hablar(self):
        print("¡Miauuu!")

class Pajaro(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
    def hablar(self):
        print("¡pio pio!")


mascotas = [Perro("picho",4),Gato("michi",3),Pajaro("coco",1)]

for mascota in mascotas:
    mascota.hablar()

