import json

datos = {
    "Nombre": "Messi",
    "Edad": 37,
    "Rol": "ING de soft",
    "Lenguajes": ["Pythoñ","JavaScript", "C++"] 
}

json_file = "persona.json"

with open(json_file,"w", encoding="UTF-8") as f:
    json.dump(datos,f,indent=4,ensure_ascii=False)

with open(json_file,"r",encoding="utf-8") as f:
    print(f.read())

#import os

#os.remove(json_file)