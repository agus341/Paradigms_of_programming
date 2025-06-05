class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def cumplir_anios(self):
        self.age += 1
    
    def show_info(self):
        print(f"Nombre: {self.name} \nEspecie: {self.species} \nEdad: {self.age} años")


while True:
    print("1. Ingresar nombre, especie y edad de la mascota")
    print("2. Mostrar información de la mascota")
    print("3. Incrementar la edad de la mascota")
    print("4. Salir")
    n = input("Ingrese la opción deseada: ")
    if n == "1":
        name = input("Ingrese nombre: ")
        species = input("Ingrese especie: ")
        age = int(input("Ingrese edad: "))
        #crea instancia
        pet = Pet(name,species,age)
    
    if n == "2":
        pet.show_info()
    
    if n == "3":
        pet.cumplir_anios()
    
    if n == "4":
        break


