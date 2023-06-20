import math
        

class Shape:
    id = 0

    def __init__(self):
        Shape.id += 1
        self.id = Shape.id
        # print("Shape constructor called.")

    def print(self):
        print(str(self.id)+ ": " + self.__class__.__name__ + ", perimeter: " + str(self.perimeter()) + ", area: " + str(self.area()))
        
    
    def perimeter(self):
        self.perimeter = 'undefined'
        return 'undefined'

    def area(self): 
        self.area = 'undefined' 
        return 'undefined'
    
    
class Circle(Shape):

    def __init__(self, radius):
        Shape.__init__(self)
        self.r = radius
        self.perimeter = self.perimeter()
        self.area = self.area()

    def perimeter(self):
        self.perimeter = 2 * self.r * math.pi
        return self.perimeter

    def area(self):
        self.area = self.r * self.r * math.pi
        return self.area
    
    def print(self):
        # print(str(self.id)+ ": " + self.__class__.__name__ + ", perimeter: " + str(self.perimeter()) + ", area: " + str(self.area()))
        print(str(self.id) + ": " + self.__class__.__name__ + ", area: {area:.5f}, perimeter: {perimeter:.5f}".format(area=self.area, perimeter=self.perimeter))
    


class Ellipse(Shape):

    def __init__(self, value1, value2):
        Shape.__init__(self)
        self.a = max(value1, value2)
        self.b = min(value1, value2)
        self.eccentricity = self.eccentricity()
        self.perimeter = self.perimeter()
        self.area = self.area()

    def area(self):
        aire = self.a * self.b 
        aire = aire * math.pi
        return aire

    def eccentricity(self):
        c = math.sqrt(self.a * self.a - self.b * self.b)
        return c
    
    def print(self):
        # print(str(self.id)+ ": " + self.__class__.__name__ + ", perimeter: " + str(self.perimeter()) + ", area: " + str(self.area()))
        print(str(self.id) + ": " + self.__class__.__name__ + ", area: {area:5f}, perimeter: " + self.perimeter+ "".format(area=self.area, perimeter=self.perimeter))


class Rhombus(Shape):

    def __init__(self, value1, value2):
        Shape.__init__(self)
        self.d1 = value1
        self.d2 = value2
        self.area = self.area()
        self.perimeter = self.perimeter()
        self.inradius = self.inradius()

    def perimeter(self):
        p = self.side()
        return 4 * p

    def area(self):
        return self.d1 * self.d2 * 0.5

    def side(self):
        ans = math.sqrt(self.d1 * self.d1 + self.d2 * self.d2)
        ans = ans / 2
        return ans

    def inradius(self):
        p = self.d1
        q = self.d2
        r = p * q / (4 * self.side())
        if r > 0:
            return r
        else:
            return None
        
    def print(self):
        # print(str(self.id)+ ": " + self.__class__.__name__ + ", perimeter: "  +  "%.2f, area: %.2f, inradius: %.2f" % (str(self.perimeter, str(self.inradius) % str(self.area))))
        print(str(self.id) + ": " + self.__class__.__name__ + ", area: {area:.0f}, perimeter: {perimeter:.0f}, inradius: {inradius:.0f}".format(area=self.area, perimeter=self.perimeter, inradius=self.inradius))
        
