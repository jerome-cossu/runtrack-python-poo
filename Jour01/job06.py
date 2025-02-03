"""Créez une classe Animal avec un attribut age initialisé à zéro et prenom
initialisé vide dans son constructeur.
Instanciez un objet Animal et affichez en console l’attribut âge. Créez une
méthode vieillir qui ajoute 1 à l'âge de l’animal. Faites vieillir votre animal et
affichez son âge mis à jour en console.

Créez une méthode nommer qui prend en paramètre le nom de l’animal.
Nommez votre animal et affichez en console son nom."""

class Animal :
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

mon_animal = Animal()

print(f"L'age de mon animal : {mon_animal.age} ans")
mon_animal.vieillir()
print(f"L'age de mon animal : {mon_animal.age} ans")

mon_animal.nommer("Melo")
print(f"Le nom de mon animal est : {mon_animal.prenom}")