class Rectangle :
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    def set_longueur(self, longueur):
        self.__longueur = longueur
    def set_largeur(self, largeur):
        self.__largeur = largeur
    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    def aire(self): 
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    def get_hauteur(self):
        return self.__hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    def volume(self):
        return self.__hauteur * self.get_longueur() * self.get_largeur()

rectangle1 = Rectangle(5, 3)
print("Perimetre du rectangle1 : ", rectangle1.perimetre())
print("Aire du rectangle1 : ", rectangle1.aire())

rectangle1.set_longueur(8)
rectangle1.set_largeur(4)

print("Nouveau perimetre du rectangle1 : ", rectangle1.perimetre())
print("Nouvelle aire du rectangle1 : ", rectangle1.aire())

parallelepipede1 = Parallelepipede(5, 3, 10)
print("Volume du parallelepipede1 : ", parallelepipede1.volume())
parallelepipede1.set_hauteur(12)

print("Nouveau volume du parallelepipede1 : ", parallelepipede1.volume())