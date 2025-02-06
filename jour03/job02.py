class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert  

    def afficher(self):
        """Affiche le détail du compte"""
        print(f"Numéro de compte: {self.__numero_compte}")
        print(f"Titulaire: {self.__prenom} {self.__nom}")
        print(f"Solde: {self.__solde} EUR")
        print(f"Découvert autorisé: {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        """Affiche uniquement le solde du compte"""
        print(f"Le solde de votre compte est de {self.__solde} EUR.")

    def versement(self, montant):
        """Effectue un versement sur le compte"""
        if montant > 0:
            self.__solde += montant
            print(f"Vous avez versé {montant} EUR sur votre compte.")

    def retrait(self, montant):
        """Effectue un retrait du compte"""
        if montant <= 0:
            print("Le montant du retrait doit être positif.")
        elif self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur : Solde insuffisant et découvert non autorisé.")

    def agios(self):
        """Applique des agios si le solde est négatif"""
        if self.__solde < 0:
            agios = abs(self.__solde) * 0.05
            self.__solde -= agios
            print(f"Des agios de {agios} EUR ont été appliqués à votre compte. Nouveau solde: {self.__solde} EUR.")

    def virement(self, compte_destinataire, montant):
        """Effectue un virement vers un autre compte"""
        if montant > 0 and self.__solde >= montant:
            self.retrait(montant)
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} EUR effectué vers le compte de {compte_destinataire.__prenom} {compte_destinataire.__nom}.")

compte1 = CompteBancaire("123456789", "Dupont", "Pierre", 1000)

compte2 = CompteBancaire("987654321", "Martin", "Lucie", -200, decouvert=True)

compte1.afficher()
compte2.afficher()

compte1.versement(500)

compte2.agios()

compte1.virement(compte2, 300)

compte1.afficherSolde()
compte2.afficherSolde()

