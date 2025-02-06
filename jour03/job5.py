import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        """Méthode qui permet à un personnage d'attaquer un autre personnage, 
        en enlevant des points de vie à l'adversaire."""
        degats = random.randint(5, 20)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

    def est_vivant(self):
        """Retourne True si le personnage est vivant, sinon False."""
        return self.vie > 0

    def afficher_etat(self):
        """Affiche l'état actuel du personnage (son nom et ses points de vie)."""
        print(f"{self.nom} a {self.vie} points de vie.")

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        """Demande au joueur de choisir un niveau de difficulté."""
        while True:
            try:
                niveau = int(input("Choisissez le niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile): "))
                if niveau in [1, 2, 3]:
                    self.niveau = niveau
                    break
                else:
                    print("Veuillez choisir un niveau entre 1 et 3.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def lancerJeu(self):
        """Lance le jeu en instanciant les personnages avec des points de vie adaptés au niveau."""
        if self.niveau == 1:
            joueur_vie = 100
            ennemi_vie = 80
        elif self.niveau == 2:
            joueur_vie = 80
            ennemi_vie = 100
        else:
            joueur_vie = 60
            ennemi_vie = 120
        
        self.joueur = Personnage("Joueur", joueur_vie)
        self.ennemi = Personnage("Ennemi", ennemi_vie)

        print(f"\nDébut du jeu :\n{self.joueur.nom} a {self.joueur.vie} points de vie.\n{self.ennemi.nom} a {self.ennemi.vie} points de vie.\n")

    def verifier_sante(self):
        """Vérifie la santé des personnages et affiche un message approprié."""
        self.joueur.afficher_etat()
        self.ennemi.afficher_etat()

    def verifier_gagnant(self):
        """Vérifie qui a gagné la partie."""
        if self.joueur.est_vivant() and not self.ennemi.est_vivant():
            print(f"\n{self.joueur.nom} a gagné !")
            return True
        elif self.ennemi.est_vivant() and not self.joueur.est_vivant():
            print(f"\n{self.ennemi.nom} a gagné !")
            return True
        return False

    def demarrer(self):
        """Démarre le jeu et gère le déroulement du combat."""
        self.choisirNiveau()
        self.lancerJeu()
        
        while not self.verifier_gagnant():
            self.joueur.attaquer(self.ennemi)
            self.verifier_sante()
            if self.verifier_gagnant():
                break

            self.ennemi.attaquer(self.joueur)
            self.verifier_sante()
            if self.verifier_gagnant():
                break

jeu = Jeu()
jeu.demarrer()
