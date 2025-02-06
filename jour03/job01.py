class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom 
        self.__habitants = habitants 

    def afficher_habitants(self):
        print(f"Population de la ville {self.__habitants}: {self.__nom}.")

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom  
        self.__age = age  
        self.__ville = ville  
    
    def ajouterPopulation(self):
        self.__ville._Ville__habitants += 1  

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

paris.afficher_habitants()
marseille.afficher_habitants()

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

paris.afficher_habitants()
marseille.afficher_habitants()