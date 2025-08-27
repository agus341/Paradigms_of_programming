class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #cuando hago print(<objeto vector>) a secas, el print busca en esta función el formato de impresión.
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"
    
    #defino la suma de objetos de tipo vector
    def __add__(self, v):
        if not isinstance(v,Vector):
            return NotImplemented
        return Vector(self.x + v.x, self.y + v.y)
    
    #defino la resta entre objetos de esta clase
    def __sub__(self,v):
        if not isinstance(v, Vector):
            return NotImplemented
        return Vector(self.x - v.x, self.y - v.y)
    
    def __mul__(self, a:float):
        return Vector(self.x * a , self.y * a)