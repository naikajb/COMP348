import math
class Shape:
    children = 0
    id = 0
    def __init__(self):
        Shape.children += 1
        id = Shape.children 
        print("Shape constructor called.")

    def print(self):
        print("Shape id: " + str(self.id))
        #print( self.__class__.__name__+ str(id))

    def perimeter(self):
        return None
    
    def area(self):
        return None
    
class Circle(Shape):
    r = 0

    def __init__(self,radius):
        Shape.__init__(self)   
        self.r = radius
    
    def perimeter(self):
        return 2 * self.r * math.pi
    
    def area(self):
        return self.r * self.r * math.pi

class Ellipse(Shape):
    a = 0
    b = 0

    def __init__(self,value1,value2):
        Shape.__init__(self)
        a = value1 if value1 > value2 else value2
        b = value2 if value1 > value2 else value1

    def area(self):
        return self.a * self.b * math.pi
    
    def eccentricity(self):
        c = math.sqrt(self.a * self.a - self.b * self.b)
        return c
    

class Rhombus(Shape):

    d1 = 0
    d2 = 0

    def __init__(self,value1,value2):
        Shape.__init__(self)
        d1 = value1
        d2 = value2

    def perimeter(self):
        return 
    
    def area(self):
        return self.d1 * self.d2 * 0.5
    
    def side(self):
        return 
    
    def inradius(self):
        return
