import math


class Shape:
    id = 0

    def __init__(self):
        id += 1
        print("Shape constructor called.")

    def print(self):
        print(self.__class__.__name__ + " with  id: " + str(self.id))
        # print( self.__class__.__name__+ str(id))

    def perimeter(self):
        return None

    def area(self):
        return None


class Circle(Shape):

    def __init__(self, radius):
        Shape.__init__(self)
        self.r = radius

    def perimeter(self):
        return 2 * self.r * math.pi

    def area(self):
        return self.r * self.r * math.pi


class Ellipse(Shape):

    def __init__(self, value1, value2):
        Shape.__init__(self)
        self.a = max(value1, value2)
        self.b = min(value1, value2)

    def area(self):
        return self.a * self.b * math.pi

    def eccentricity(self):
        c = math.sqrt(self.a * self.a - self.b * self.b)
        return c


class Rhombus(Shape):

    def __init__(self, value1, value2):
        Shape.__init__(self)
        self.d1 = value1
        self.d2 = value2

    def perimeter(self):
        return 4 * self.side()

    def area(self):
        return self.d1 * self.d2 * 0.5

    def side(self):
        return math.sqrt(self.d1 * self.d1 + self.d2 * self.d2) / 2

    def inradius(self):
        p = self.d1
        q = self.d2
        r = p * q / (4 * self.side())
        if r > 0:
            return r
        else:
            return None
