"""Créez une classe nommée Point avec les attributs x et y correspondant aux
coordonnées horizontales et verticales du point. Les deux attributs doivent
être initialisés dans le constructeur.
La classe Point doit posséder les méthodes suivantes :
➔ afficherLesPoints qui affiche les coordonnées des points.
➔ afficherX et afficherY qui affiche respectivement x et y.
➔ changerX et changerY qui change la valeur des attributs x et y."""

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def afficherLesPoints(self):
        print(f"Le point a pour coordonnées : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée X : {self.x}")

    def afficherY(self):
        print(f"Coordonnée Y : {self.y}")

    def changerX(self, nouvelleX):
        self.x = nouvelleX

    def changerY(self, nouvelleY):
        self.y = nouvelleY 

point1 = Point(3, 4)
point2 = Point(7, 1)

point1.afficherLesPoints()
point2.afficherLesPoints() 

point1.afficherX()
point2.afficherX() 

point1.afficherY()
point2.afficherY() 

point1.changerX(10)
point1.changerY(20) 

point1.afficherLesPoints()
