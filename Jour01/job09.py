"""Créez la classe Produit avec des attributs nom, prixHT, TVA. Implémentez la
méthode CalculerPrixTTC qui retourne le prix produit avec la TVA. Ajoutez la
méthode afficher qui liste l’ensemble des informations du produit.
Créez plusieurs produits et calculez leurs TVA.
Ajoutez des méthodes permettant de modifier le nom du produit et son prix.
Ainsi que des méthodes permettant de retourner chaque information du
produit.
Modifiez le nom et le prix de chaque produit et affichez en console le nouveau
prix des produits.
La fonction print() ne doit pas être utilisée dans la classe Produit.
Sur vos scripts doit apparaître l’ensemble des méthodes appelées tout au
long des exercices."""
class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom: {self.nom}\nPrix HT: {self.prixHT}€\nTVA: {self.TVA}%\nPrix TTC: {self.calculerPrixTTC()}€"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.calculerPrixTTC()

produit1 = Produit("Ordinateur Portable", 800, 20)
produit2 = Produit("Smartphone", 500, 15)
produit3 = Produit("Casque Audio", 100, 5)

print("Produit 1:")
print(produit1.afficher())
print()

print("Produit 2:")
print(produit2.afficher())
print()

print("Produit 3:")
print(produit3.afficher())
print()

produit1.modifierNom("Ordinateur de Bureau")
produit1.modifierPrix(900)

produit2.modifierNom("Smartphone Pro")
produit2.modifierPrix(550)

produit3.modifierNom("Casque Audio Sans Fil")
produit3.modifierPrix(120)

print("Produit 1 modifié:")
print(produit1.afficher())
print()

print("Produit 2 modifié:")
print(produit2.afficher())
print()

print("Produit 3 modifié:")
print(produit3.afficher())
