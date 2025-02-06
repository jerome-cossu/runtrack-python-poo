class Tache :
    def __init__(self, titre, description, statut = "à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
    def marquer_comme_finie(self):
        self.statut = "terminé"
    def __str__(self):
        return f"Tâche : {self.titre}\n Description : {self.description}\n Statut : {self.statut}"

class ListeDeTaches :
    def __init__(self):
        self.taches = []
    def ajouter_tache(self, tache):
        self.taches.append(tache)
    def suprimer_tache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
    def marquer_comme_finie(self, tache):
        if tache in self.taches:
            tache.marquer_comme_finie()
    def afficher_liste(self):
        for tache in self.taches:
            print(tache)
    def filter_liste(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]
    
tache1 = Tache("Acheter du lait", "Acheter de lait pour la semaine")
tache2 = Tache("Faire une lessive", "Lancer une machine des draps")
tache3 = Tache("Finir ma runtrack", "Faire ma runtrack Python sur l'héritage")

liste = ListeDeTaches()

liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)
liste.ajouter_tache(tache3)

print("Tâches a réaliser :")
liste.afficher_liste()

liste.marquer_comme_finie(tache2)
print("\nTâche terminée")

liste.suprimer_tache(tache1)
print("\nTâches à réaliser après suppression : ")
liste.afficher_liste()

print("\nTâches à faire : ")
for tache in liste.filter_liste("à faire"):
    print(tache)