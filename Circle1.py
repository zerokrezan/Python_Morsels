import math

class Circle():
    def __init__(self, radius=1):
        self.Radius = radius
        self.Diameter= (2*self.Radius)
        self.Area = (math.pi * self.Radius**2)

    def __repr__(self):
        return f"Circle({self.Radius})"  


c = Circle() 
print(c)


