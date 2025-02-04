class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut = "en cours" 

    def get_numero_commande(self):
        return self.__numero_commande

    def get_statut(self):
        return self.__statut

    def get_plats_commandes(self):
        return self.__plats_commandes

    def ajouter_plat(self, nom_plat, prix):
        if self.__statut != "annulée":
            self.__plats_commandes[nom_plat] = {"prix": prix, "statut": "en attente"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")

    def annuler_commande(self):
        if self.__statut != "terminée":
            self.__statut = "annulée"
            print("La commande a été annulée.")

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            total += plat["prix"]
        return total

    def afficher_commande(self):
        if self.__statut != "annulée":
            print(f"Commande n° {self.__numero_commande} - Statut: {self.__statut}")
            print("Plats commandés :")
            for nom, details in self.__plats_commandes.items():
                print(f"  - {nom} : {details['prix']}€")
            total = self.__calculer_total()
            print(f"Total à payer : {total}€")

    def calculer_tva(self, taux_tva=0.20):
        total = self.__calculer_total()
        tva = total * taux_tva
        print(f"TVA à {taux_tva * 100}% : {tva}€")
        return tva

commande1 = Commande(53)

commande1.ajouter_plat("McExtreme avec grande frite", 12.50)
commande1.ajouter_plat("Big-Mac avec moyenne potatoes", 11.00)

commande1.afficher_commande()

commande1.calculer_tva()

commande1.annuler_commande()

commande1.ajouter_plat("McFleury Pistachio ", 4.00)
