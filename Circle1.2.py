import math

class Circle:
    def __init__(self, radius=1):
        self.Radius = radius

    def radius(self):
        return(self.Radius)   

    def __repr__(self):                                                            
        return f"Circle({self.Radius})"

    def diameter(self):
        return 2*self.Radius

    def area(self):
        return(math.pi *self.Radius**2)

c = Circle()
print(c)
print(c.radius())
print(c.diameter())
print(c.area())
