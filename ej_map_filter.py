lista = [1,2,3,4,4,3,2,1]
print(list(filter(lambda x: x%4 == 0, lista)))

#todo a mayúscula

texto = "hola mundo xd"
print(str(list(map(lambda x: x.upper(), texto))))

# multiplicar todos elementos
from functools import reduce
print(reduce(lambda x,y: x*y,lista))

# multiplicador

def crea_multiplicador(y):
    def multiplicador(x):
        return x*y
    return multiplicador

multiplica_por_3 = crea_multiplicador(3)
print(f"3*4 = {multiplica_por_3(4)}")

# Contador
def contador():
    #inicializa el contador en 0, el primer print será en cero
    cuenta = 0
    def siguiente():
        nonlocal cuenta #importa desde contador la variable cuenta
        cuenta += 1
        return cuenta #retorna cuenta a la funcion externa (actualiza el valor)
    return siguiente

contador1 = contador()
print(contador1())
print(contador1())
print(contador1())
print(contador1())

contador2 = contador()
print(contador2())
print(contador2())
print(contador2())
print(contador2())