class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nModele: {self.modele}\nAnnee: {self.annee}\nPrix: {self.prix}")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")
    def demarrer(self):
        print("La voiture démarre")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")
    def demarrer(self):
        print("La moto démarre")

voiture1 = Voiture("Peugeot", "208", 2020, 65000)
voiture1.informationsVehicule()
voiture1.demarrer()
moto1 = Moto("Yamaha", "MT-07", 2019, 8000)
moto1.informationsVehicule()
moto1.demarrer()

