from ejercicio1_clases import Pet

class PruebaPrivacidad:
    def __init__(self,a,b,c):
        self._a = a
        self.__b = b
        self.c = c
    
    def getb(self):
        return self.__b
    
if __name__ == "__main__":
    o = PruebaPrivacidad(1,2,3)
    p = Pet("a","b",1)
    print(o._PruebaPrivacidad__b)
    print(p.age)
    print(type(o))
    print(type(p))



