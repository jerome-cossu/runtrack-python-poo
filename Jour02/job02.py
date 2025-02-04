"""Créer la classe Livre qui prend en attributs privés un titre, un auteur et un
nombre de pages.
Créer les accesseurs et mutateurs nécessaires afin de pouvoir modifier et
afficher les attributs. Pour changer le nombre de pages, ce dernier doit être
un nombre entier positif, sinon la valeur n’est pas changée et un message
d’erreur est affiché."""

class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    def get_titre(self):
        return self.__titre   
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages
    def set_nombre_de_pages(self, nombre_de_pages):
        self.__nombre_de_pages = nombre_de_pages

    def lecture(self):
        print(f"Le livre est {self.__titre}\nIl est écrit par {self.__auteur}\nIl y a {self.__nombre_de_pages}")

mon_livre = Livre ("Plus Grands Que Le Ciel", "Virginie Grimaldi", 337)

mon_livre.lecture()

mon_livre.set_titre("Tout Le Bleu Du Ciel")
mon_livre.set_auteur("Mélissa Da Costa")
mon_livre.set_nombre_de_pages(850)

mon_livre.lecture()
        