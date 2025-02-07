import random


class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valet', 'Dame', 'Roi', 'As']
        self.paquet = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]
        random.shuffle(self.paquet)

    def distribuer(self, joueur):
        """Distribue 2 cartes à un joueur."""
        joueur.main = [self.paquet.pop(), self.paquet.pop()]

    def prendre_carte(self, joueur):
        """Donne une carte au joueur."""
        joueur.main.append(self.paquet.pop())

    def calculer_score(self, main):
        """Calcule le score total d'une main."""
        score = 0
        as_count = 0
        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                score += 10
            elif carte.valeur == 'As':
                score += 11
                as_count += 1
            else:
                score += carte.valeur
        while score > 21 and as_count:
            score -= 10
            as_count -= 1

        return score

    def afficher_main(self, joueur):
        """Affiche la main du joueur."""
        print(f"Main de {joueur.nom}:")
        for carte in joueur.main:
            print(carte)
        print(f"Score: {self.calculer_score(joueur.main)}")

    def afficher_paquet(self):
        """Affiche toutes les cartes restantes dans le paquet."""
        for carte in self.paquet:
            print(carte)

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
    def choix(self):
        """Demande au joueur s'il veut 'prendre' une carte ou 'passer'."""
        choix = input(f"{self.nom}, voulez-vous 'prendre' une carte ou 'passer'? ")
        return choix.lower()

def jouer():
    jeu = Jeu()
    joueur = Joueur("Joueur")
    croupier = Joueur("Croupier")
    jeu.distribuer(joueur)
    jeu.distribuer(croupier)
    jeu.afficher_main(joueur)
    print(f"\nCoup du croupier : {croupier.main[0]} et une carte cachée\n")
    while jeu.calculer_score(joueur.main) < 21:
        choix = joueur.choix()
        if choix == 'prendre':
            jeu.prendre_carte(joueur)
            jeu.afficher_main(joueur)
        elif choix == 'passer':
            break
        else:
            print("Choix invalide. Veuillez entrer 'prendre' ou 'passer'.")
            continue
    if jeu.calculer_score(joueur.main) > 21:
        print(f"\n{joueur.nom} a dépassé 21. Le croupier gagne !")
        return
    print("\nTour du croupier:")
    jeu.afficher_main(croupier)
    while jeu.calculer_score(croupier.main) < 17:
        print("Le croupier prend une carte...")
        jeu.prendre_carte(croupier)
        jeu.afficher_main(croupier)
    score_joueur = jeu.calculer_score(joueur.main)
    score_croupier = jeu.calculer_score(croupier.main)
    print(f"\nScores finaux - {joueur.nom}: {score_joueur}, Croupier: {score_croupier}")
    if score_croupier > 21:
        print(f"\nLe croupier a dépassé 21. {joueur.nom} gagne !")
    elif score_joueur > score_croupier:
        print(f"\n{joueur.nom} gagne !")
    elif score_joueur < score_croupier:
        print(f"\nLe croupier gagne !")
    else:
        print("\nMatch nul !")

if __name__ == "__main__":
    jouer()
