import math

class Forme :
    def __init__(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    def aire(self):
        return math.pi * (self.radius ** 2)

cercle1 = Cercle(4)
print("L'aire du cercle est de", cercle1.aire())