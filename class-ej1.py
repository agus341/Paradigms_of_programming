# Definición de la clase Person:
class Person:
    # self es una referencia al propio objeto de la clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nombre_completo = f"{nombre} {apellido}"

    def walk(self):
        print(f"{self.nombre_completo} está caminando")

    def talk(self):
        print(f"{self.nombre_completo} está hablando")

mi_person = Person("Agustin", "Jesus", 67)    # Instancia de la clase Person

#mi_person.nombre = "Agustin"
#mi_person.apellido = "Jesus"
#mi_person.edad = 67
print(mi_person.nombre)
print(mi_person.apellido)
print(mi_person.edad)
print(mi_person.nombre_completo)

mi_person.talk()
mi_person.walk()