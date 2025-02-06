import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    def attaquer(self, adversaire):
        degats = random.randint(5, 20)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
    def est_vivant(self):
        return self.vie > 0
    def afficher_etat(self):
        print(f"{self.nom} a {self.vie} points de vie.")

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None
    def choisirNiveau(self):
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
        if self.niveau == 1:
            joueur_vie = 100
            ennemi_vie = 80
        elif self.niveau == 2:
            joueur_vie = 80
            ennemi_vie = 100
        else:
            joueur_vie = 60
            ennemi_vie = 120   
        self.joueur = Personnage("Naruto", joueur_vie)
        self.ennemi = Personnage("Sasuke", ennemi_vie)
        print(f"\nDébut du jeu :\n{self.joueur.nom} a {self.joueur.vie} points de vie.\n{self.ennemi.nom} a {self.ennemi.vie} points de vie.\n")
    def verifier_sante(self):
        self.joueur.afficher_etat()
        self.ennemi.afficher_etat()
    def verifier_gagnant(self):
        if self.joueur.est_vivant() and not self.ennemi.est_vivant():
            print(f"\n{self.joueur.nom} a gagné !")
            return True
        elif self.ennemi.est_vivant() and not self.joueur.est_vivant():
            print(f"\n{self.ennemi.nom} a gagné !")
            return True
        return False
    def demarrer(self):
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
