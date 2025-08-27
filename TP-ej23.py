# Ejercicio 23: Clases, Objetos y Funciones Avanzadas en Python

# Crear un sistema sencillo de gestión bancaria usando programación orientada a objetos 
# y funciones avanzadas en Python.

# 1. Define una clase llamada `Cuenta`: 
#   - Cada cuenta debe tener como atributos:  
#     - `titular` (nombre del cliente, tipo string)
#     - `saldo` (saldo de la cuenta, tipo numérico)
#     - `id` (identificador único que se asigne automáticamente a cada cuenta nueva)
#   - Implementa el método especial `__str__` para mostrar la información de la cuenta 
#     de forma legible, por ejemplo:  
#     `"ID: 1 | Titular: Ana | Saldo: 1500"`
#   - Implementa el método especial `__eq__` para poder comparar si dos cuentas tienen 
#     el mismo saldo (deben retornar `True` si los saldos son iguales).
class Cuenta:
    def __init__(self,titular,saldo,id):
        self.titular = titular
        self.saldo = saldo
        self.id = id

    def __str__(self):
        return f"ID: {self.id} | Titular: {self.titular} | Saldo: {self.saldo}"
    
    def __eq__(self,otro):
        return self.saldo == otro.saldo


class Cuenta2:
    _id = 0
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        self.id = Cuenta2._id
        Cuenta2._id += 1
    

    def __str__(self):
        return f"ID: {self.id} | Titular: {self.titular} | Saldo: {self.saldo}"
    
    def __eq__(self,otro):
        return self.saldo == otro.saldo

# 2. Define una clase llamada `Banco`: 
#   - Debe tener un atributo que almacene una lista de cuentas (`self.cuentas`).
#   - Implementa un método `agregar_cuenta(titular, saldo_inicial)` que cree una nueva 
#     cuenta y la agregue a la lista.
#   - Implementa un método `mostrar_cuentas_ordenadas()` que muestre todas las cuentas 
#     ordenadas por saldo ascendente (usa la función `sorted` y una lambda como clave).
#   - Implementa un método `mostrar_cuentas_filtradas(monto)` que muestre solo las 
#     cuentas cuyo saldo sea mayor al monto recibido (usa `filter` y una lambda).
#   - Implementa un método `buscar_cuenta_por_titular(titular)` que devuelva la cuenta 
#     correspondiente al titular.
#   - Implementa un método `generar_aplicador_interes(titular, interes)` que devuelva 
#     una función (closure) que, al ejecutarse, aplique el interés (por ejemplo, 0.05 
#    para 5%) al saldo de la cuenta del titular indicado.  
#     - Si la cuenta no existe, la función devuelta debe informar que el titular no fue 
#       encontrado.
class Banco:
    cuentas = []

    def agregar_cuenta(self,titular,saldo_inicial):
        self.cuentas.append(Cuenta(titular,saldo_inicial,len(self.cuentas)))

    def mostrar_cuentas_ordenadas(self):
        ls_sorted = sorted(self.cuentas, key= lambda x: x.saldo)
        for cuenta in ls_sorted:
            print(cuenta)
    
    def mostrar_cuentas_filtradas(self,monto):
        print(*list(filter(lambda x: x.saldo > monto, self.cuentas)), end= "\n")

    def buscar_cuenta_por_titular(self,titular):
        print(*list(filter(lambda x: x.titular == titular, self.cuentas)), end ="\n\n")

    def generar_aplicador_interes(self,titular):
        cuenta = list(filter(lambda x: x.titular == titular, self.cuentas))
        if len(cuenta) != 0:
            def aplicar_interes(interes):
                cuenta[0].saldo =+ cuenta[0].saldo * (1+interes)
            return aplicar_interes
        else:
            print("Cuenta de titular no encontrada")

            
class Banco2:
    cuentas = []

    def agregar_cuenta(self,titular,saldo_inicial):
        self.cuentas.append(Cuenta2(titular,saldo_inicial))

    def mostrar_cuentas_ordenadas(self):
        print("Estas son las cuentas ordenadas por saldo")
        for cuenta in sorted(self.cuentas, key= lambda x: x.saldo):
            print(cuenta)
    
    def mostrar_cuentas_filtradas(self,monto):
        print(*list(filter(lambda x: x.saldo > monto, self.cuentas)),sep= "\t")

    def buscar_cuenta_por_titular(self,titular):
        print(*list(filter(lambda x: x.titular == titular, self.cuentas)), end ="\n\n")

    def generar_aplicador_interes(self,titular):
        cuenta = list(filter(lambda x: x.titular == titular, self.cuentas))
        if len(cuenta) != 0:
            def aplicar_interes(interes):
                cuenta[0].saldo =+ cuenta[0].saldo * (1+interes)
            return aplicar_interes
        else:
            print("Cuenta de titular no encontrada")


    

### Ayuda

# - Usa una variable de clase o contador estático para generar IDs únicos en `Cuenta`.
# - Para ordenar o filtrar listas, recuerda que puedes usar `sorted(lista, key=...)` 
#   y `filter(funcion, lista)`.
# - Las funciones lambda pueden ayudarte a definir funciones pequeñas y rápidas, 
#   por ejemplo, para filtrar o para la clave de ordenamiento.
# - Un closure es una función interna que recuerda el contexto donde fue creada 
#   (por ejemplo, la cuenta a la que debe aplicar el interés).

credicoop = Banco2()

credicoop.agregar_cuenta("agustin",1000)
credicoop.agregar_cuenta("gonza",1500)
credicoop.agregar_cuenta("tomi",2000)
credicoop.agregar_cuenta("belu",2500)
credicoop.agregar_cuenta("emi",3000)
credicoop.agregar_cuenta("valen",3500)

credicoop.mostrar_cuentas_filtradas(2000)
credicoop.buscar_cuenta_por_titular("agustin")
credicoop.mostrar_cuentas_ordenadas()
credicoop.generar_aplicador_interes("agustin")(0.05)
credicoop.buscar_cuenta_por_titular("agustin")

print(Cuenta2("agus",5000))
print(Cuenta2("agus",5000))
print(Cuenta2("agus",5000))

