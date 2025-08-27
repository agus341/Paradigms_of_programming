# Clase Estudiante
class Student:
    def __init__(self, name, age, carreer):
        self.name = name
        self.age = age
        self.carrer = carreer
        self.califications = []

    def add_calification(self, calification):
        self.califications.append(calification)  #Agrega la calificación a la list
    
    def average_calculate(self):
        if len(self.califications)!= 0:
            acum = 0
            for calif in self.califications:
                acum += calif
            prom = acum / len(self.califications)
        else:
            prom = 0
        return prom
            

    def show_info(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Carrera: {self.carrer}")
        print(f"Promedio: {self.average_calculate()}")

name = input("Ingrese nombre: ")
age = int(input("Ingrese la edad: "))
carreer = input("Ingrese la carrera: ")
student = Student(name, age, carreer)

while True:
    print("\n1.Agregar calificaciones: ")
    print("2.Mostrar informacion del estudiante: ")
    a = input("Ingrese la opcion: ")
    if a == "1":
        calification = float(input("Ingrese la calificación: "))
        student.add_calification(calification)
    elif a == "2":
        student.show_info()
    else:
        break
