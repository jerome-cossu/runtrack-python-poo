"""Créer une classe Rectangle avec des attributs privés, longueur et largeur
initialisées dans le constructeur.
Créer des accesseurs et mutateurs afin de pouvoir afficher et modifier les
attributs de la classe.

Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5.
Changer la valeur de la longueur et de la largeur et vérifier que les
modifications soient bien prises en compte."""

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