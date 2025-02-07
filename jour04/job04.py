class Forme :
    def __init__(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def aire(self):
        return self.largeur * self.hauteur

rectangle1 = Rectangle(5, 3)
print("L'aire du rectangle est de", rectangle1.aire())
    
        