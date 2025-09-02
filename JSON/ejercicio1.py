
class Persona:
    def __init__(self,nombre,edad,rol,lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol
        self.lenguajes = lenguajes
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nRol: {self.rol}\nLenguajes: {', '.join(self.lenguajes)}"

import json

json_file = "persona.json"

#Extraer información del json
with open(json_file, 'r') as f:
    datos = json.load(f)

lista = []
for valor in datos.values():
    lista.append(valor)

persona = Persona(*lista)

print(persona)


#cargar una persona desde mi objeto al json
datos2 = {'Nombre': persona.nombre, 'Edad': persona.edad, 'Rol': persona.rol, 'Lenguajes': persona.lenguajes}
with open(json_file,"w",encoding="utf-8") as f:
    json.dump(datos2,f,indent=4,ensure_ascii=False)


#cargar dos o más personas a un json
datos3 = [
        {'Nombre': persona.nombre, 'Edad': persona.edad, 'Rol': persona.rol, 'Lenguajes': persona.lenguajes},
        {'Nombre': persona.nombre, 'Edad': persona.edad, 'Rol': persona.rol, 'Lenguajes': persona.lenguajes},
        {'Nombre': persona.nombre, 'Edad': persona.edad, 'Rol': persona.rol, 'Lenguajes': persona.lenguajes}
    ]

with open(json_file,"w",encoding="utf-8") as f:
    json.dump(datos3,f,indent=4,ensure_ascii=False)

#si se quiere traer desde un archivo json,
#lo devuelve como una lista de diccionarios






