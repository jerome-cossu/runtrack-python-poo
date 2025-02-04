class Voiture :
    def __init__(self, marque, modele, annee, kilometrage ):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele
    def set_modele(self, modele):
        self.__modele = modele
    
    def get_annee(self):
        return self.__annee
    def set_annee(self, annee):
        self.__annee = annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
    
    def get_reservoir(self):
        return self.__reservoir
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir
    
    def demarrer (self):
        if self.__verifier_plein():
            self.__en_marche = True
            print(f"La voiture {self.__marque}, {self.__modele} a bien démarré")
    def arreter(self):
        self.__en_marche = False
        print(f"La voiture {self.__marque}, {self.__modele} est arrêtée")
    def __verifier_plein(self):
        if self.__reservoir > 5:
            return True
        else :
            return False

voiture1 = Voiture("Peugeot", 208, 2020, 60000)

print(voiture1.get_en_marche())

voiture1.demarrer()

print(voiture1.get_en_marche)

voiture1.arreter()