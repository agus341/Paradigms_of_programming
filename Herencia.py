class Animal:
    def __init__(self,nombre,edad,especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}")

class Leon(Animal):
    def __init__(self,nombre,edad,especie,duenio):
        super().__init__(nombre,edad,especie)
        self.duenio = duenio

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Dueño: {self.duenio}")