import xml.etree.ElementTree as ET

datos = {
    "Nombre": "Messi",
    "Edad": 37,
    "Nacimiento": "1987-06-24",
    "Lenguajes": ["Pythoñ","JavaScript", "C++"] 
}

#Crear XML
xml_file = "persona.xml"
root = ET.Element("Persona")
ET.SubElement(root,"Nombre").text = datos["Nombre"]
ET.SubElement(root,"Edad").text = str(datos["Edad"])
ET.SubElement(root,"Nacimiento").text = datos["Nacimiento"]

tree = ET.ElementTree(root)
tree.write(xml_file,encoding="utf-8",xml_declaration=True)

#Mostrar contenido
with open(xml_file,"r",encoding="utf-8") as f:
    print(f.read())

#Borrar archivo
import os
os.remove(xml_file)
# with open(xml_file,"r",encoding="utf-8") as f: --- IGNORE ---
#     print(f.read())

