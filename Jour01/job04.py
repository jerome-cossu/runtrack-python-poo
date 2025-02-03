"""Créez une classe Personne avec les attributs nom et prenom. Ajoutez une
méthode SePresenter qui retourne le nom et le prénom de la personne.
Ajoutez aussi un constructeur prenant en paramètres de quoi donner des
valeurs initiales aux attributs nom et prenom. Instanciez plusieurs personnes
avec les valeurs de construction de votre choix et faites appel à la méthode
SePresenter afin de vérifier que tout fonctionne correctement."""

class Personne :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def Sepresenter(self):
        return f"Je suis {self.prenom}{self.nom}"
personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")

print(personne1.Sepresenter())
print(personne2.Sepresenter())
        