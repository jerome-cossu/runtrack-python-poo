"""Récupérer la classe Livre.
Ajouter l'attribut privé suivant :
- disponible est initialisé par défaut à True.
Créer une méthode nommée vérification qui vérifie si le livre est disponible,
c'est-à-dire que la valeur de son attribut disponible est égale à True. Cette
méthode doit retourner True ou False.
Ajouter une méthode emprunter qui rend le livre indisponible, autrement dit
la valeur de disponible devient False. Bien sûr, pour pouvoir emprunter un
livre, il faut que celui-ci soit disponible, vérifiez donc que celui-ci soit
disponible sans utiliser l’attribut disponible.
Après avoir emprunté un livre, il faut pouvoir le rendre. Créer une méthode
rendre qui dans un premier temps vérifie si le livre a bien été emprunté ( sans
utiliser l’attribut disponible), puis change la valeur de l’attribut disponible."""

class Livre:
    def __init__(self, titre):
        self.titre = titre
        self.__disponible = True
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"Le livre {self.titre} est déjà emprunter")
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"Le livre {self.titre} a été rendu")

livre1 = Livre("Tu Comprendras Quand Tu Seras Grande")   

livre1.emprunter()

livre1.rendre()

print(livre1.verification())