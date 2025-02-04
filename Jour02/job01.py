class Rectangle:
    def __init__(self, longueur, lagreur):
        self.__longueur = longueur
        self.__largeur = lagreur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

    def dimensions(self):
        print(f"La longueur est de : {self.__longueur}\nLa largeur est de : {self.__largeur}")

rectangle1 = Rectangle(10, 5)

rectangle1.dimensions()

rectangle1.set_longueur(15)
rectangle1.set_largeur(7)

rectangle1.dimensions()