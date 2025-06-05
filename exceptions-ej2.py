

try:
    with open("notas.txt","r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue #regresa al for
            try:
                nombre, nota = linea.split(",")
                nombre = nombre.strip()
                nota = float(nota.strip())
                print(f"Alumna/o: {nombre} | Nota: {nota}")
            except Exception:
                print(f"Error en la linea: {linea}. Formato incorrecto")
except FileNotFoundError:
    print("Error: El archivo no existe.")

print("Fin del programa.")