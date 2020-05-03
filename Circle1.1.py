import math

class Circle:
    def __init__(self, radius=1):
        self.Radius = radius

    def radius(self):
        print(self.Radius)   

    def __repr__(self):                                         # '__repr__() ' is an own specific method in python!
        return f"Circle({self.Radius})"
    
    def diameter(self):
        print(2*self.Radius)

    def area(self):
        print(math.pi *self.Radius**2)

c = Circle()
print(c)
c.radius()
c.diameter()
c.area()
