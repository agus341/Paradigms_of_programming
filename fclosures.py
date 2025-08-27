print("\n***closures***")

def suma_diez(y): #función externa 
    def suma(x):  #función interna o closure. Recuerda el contexto de creación (argumentos de la función externa).
        return y + x + 10
    return suma

sum = suma_diez(1)
print(sum(2))
print(suma_diez(1)(2))
      

def crear_saludo(saludo):
    def saludar(nombre):
        return f"{saludo}, {nombre}"
    return saludar

saludo1 = crear_saludo("hola buenas tardes")
print(saludo1("Juan"))
print(saludo1("Juani"))