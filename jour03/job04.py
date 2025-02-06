class Joueur :
    def __init__(self, nom, prénom, position):
        self.nom = nom
        self.prenom = prénom
        self.position = position
        self.buts = 0
        self.passe_de = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
    def marquerUnBut(self):
        self.buts += 1
    def effectuerUnePasseDecisive(self):
        self.passe_de += 1
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    def afficherStatistique(self):
        print(f"Voici les statistique de {self.prenom}, {self.nom}\nNombre de buts : {self.buts}\nPasses décisives : {self.passe_de}\nCartons jaunes : {self.cartons_jaunes}\nCartons rouges : {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    def afficherSatistiquesJoueurs(self):
        print(f"Stats de joueurs de {self.nom}")
        for joueur in self.joueurs:
            joueur.afficherStatistique()
    def mettreAJourStatistiqueJoueur(self, joueur, action):
        if action == "but":
            joueur.marquerUnBut()
        elif action == "passe_decisive":
            joueur.effectuerUnePasseDecisive()
        elif action == "carton_jaune":
            joueur.recevoirUnCartonJaune()
        elif action == "carton_rouge":
            joueur.recevoirUnCartonRouge()

joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Andres Iniesta", 8, "Milieu")
joueur3 = Joueur("Xavi Hernadez", 6, "Milieu")
joueur4 = Joueur("Carles Puyol", 2, "Défensseur")

equipe = Equipe("FC Barcelonna")

equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)
equipe.ajouterJoueur(joueur4)

equipe.afficherSatistiquesJoueurs()

equipe.mettreAJourStatistiqueJoueur(joueur1, "but")
equipe.mettreAJourStatistiqueJoueur(joueur1, "but")
equipe.mettreAJourStatistiqueJoueur(joueur2, "passe_decisive")
equipe.mettreAJourStatistiqueJoueur(joueur3, "but")
equipe.mettreAJourStatistiqueJoueur(joueur4, "carton_rouge")

print("\nAprès le match :")
equipe.afficherSatistiquesJoueurs()