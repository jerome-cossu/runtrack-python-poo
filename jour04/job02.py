class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")

class Eleve(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)
    def allerEnCours(self):
        print(f"{self.nom} : Je vais en cours.")

class Professeur(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)
    def enseigner(self):
        print(f"{self.nom} : Commence le cours.")

eleve = Eleve("Alice", 14)
eleve.bonjour()
eleve.allerEnCours()
eleve.age = 15
professeur = Professeur("Monsieur Dupont", 40)
professeur.bonjour()
professeur.enseigner() 
