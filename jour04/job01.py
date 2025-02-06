class Personne:
    def __init__(self, age=14):
        self.age = age
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    def bonjour(self):
        print("Hello")
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age
class Eleve(Personne):
    def __init__(self, age=14):
        super().__init__(age)
    def allerEnCours(self):
        print("Je vais en cours")
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    def enseigner(self):
        print("Le cours va commencer")   
    def getMatiereEnseignee(self):
        return self.__matiereEnseignee
    
personne = Personne()
personne.afficherAge() 
eleve = Eleve()
eleve.afficherAge()
prof = Professeur("Mathématiques")  
print(f"Le professeur enseigne : {prof.getMatiereEnseignee()}")  
prof.enseigner()
