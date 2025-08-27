#quiero hacer una calculadora de operaciones matematicas
#que haga las operaciones de suma, resta, multiplicacion y division
#que reciba dos numeros y una operacion y devuelva el resultado


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculadora(a, b, operacion):
    if operacion == "suma":
        return suma(a, b)
    elif operacion == "resta":
        return resta(a, b)
    elif operacion == "multiplicacion":
        return multiplicacion(a, b)
    elif operacion == "division":
        return division(a, b)
    else:
        return "Error: Operacion no valida"
    










