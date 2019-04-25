# On va faire un jeu de cartes en utilisant la POO 

from random import *

##Initiation d'une liste et d'un dictionnaire avec les valeurs des cartes pour la bataille
listeCouleurs = ["♠", "♥", "♦", "♣"]
dicoRangs = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "Valet": 11,
    "Dame": 12,
    "Roi": 13,
    "As":14
}

# On crée une classe pour créer une carte

class Carte:
    def __init__(self, couleur, rang, valeur):
        self.valeur = valeur
        self.nom = "{0} de {1}".format(rang, couleur)

# Crée une instance de carte et informe du nom de la carte et de sa valeur
carte1 = Carte("pique", "dame", 12)
print(carte1.nom, "vaut", carte1.valeur, "points")

# On va créer une classe Jeu qui va boucler la liste des couleurs et le dictionnaire des rangs pour construire un jeu de 52 cartes
# Cette classe va comporter un dictionnaire pour associer les valeurs à chaque nom de carte, ex. Valet de trefle : 11
# Cette classe va aussi comporter une liste de toutes les cartes qui nous servira à mélanger le jeu de cartes
class Jeu:
    def __init__(self):
        self.jeuComplet = {}
        self.listeDuJeu = []
        for couleur in listeCouleurs: 
            for cleRang, valeurRang in dicoRangs.items():
                rang = cleRang
                valeur = valeurRang
                carte = Carte(couleur, rang, valeur)
                self.jeuComplet[carte.nom] = valeur
                self.listeDuJeu.append(carte.nom)

    # def battre(self):
    #     shuffle(self.listeDuJeu)

    # def tirerCarte(self, n):
    #     """Tire la carte suivante"""
    #     return self.listeDuJeu[n]


 # On peut créer une instance de Jeu et afficher le jeu pour vérifier s'il est bien construit  
monJeu = Jeu()
print(monJeu.jeuComplet)

# Ajoute ensuite une fonction pour mélanger le jeu à la classe Jeu, n'oublie pas d'importer la librairie random
monJeu.battre()
print(monJeu.listeDuJeu)

# Ajoute maintenant une fonction qui prendra en paramètre l'index de la listeDuJeu pour tirer une carte dans le jeu mélangé et teste-là
carte2 = monJeu.tirerCarte(0)
print(carte2)

# Voilà, nous allons pouvoir commencer la bataille ! Crée une fonction qui lancera une battaille entre 2 joueurs, pour cela il te faudra une classe Joueur pour créer un joueur qui dépendra de la classe Jeu. Cette classe Joueur aura 2 propriétés : un nom de joueur (passé en paramètre) et un total de points. 

class Joueur(Jeu):
    """Classe des joueurs"""
    def __init__(self, nom):
        Jeu.__init__(self)
        self.nom = nom
        self.points = 0

# On peut donc créer 2 joueurs et afficher leurs noms et leurs points :
j1 = Joueur("Luke")
j2 = Joueur("Dark Vador")
print(j1.nom, "a", j1.points, "points et", j2.nom, "a", j2.points, "points")

# Comme elle dépend de Jeu, elle héritera aussi de ses caractéristiques. Utilise la fonction pour mélanger le jeu de joueur1, affiche le jeu mélangé et affiche une carte tiré avec l'index 0 : 
j1.battre()
print(j1.listeDuJeu)
print(j1.tirerCarte(0), j2.tirerCarte(0))

# Crée la fonction pour la bataille, ici je te laisse réfléchir à l'algorithmie... 
def bataille(n):
    """Lancer la bataille entre 2 cartes"""
    if(n < 52):
        carte1 = j1.tirerCarte(n)
        c1Valeur = j1.jeuComplet[carte1]
        carte2 = j2.tirerCarte(n)
        c2Valeur = j2.jeuComplet[carte2]
        print("\n" + j1.nom, "votre carte est :", carte1)
        print("La carte de", j2.nom, "est :", carte2)
        if c1Valeur > c2Valeur:
            print ("\n" + carte1 + " est plus grand que " + carte2)
            j1.points +=1
            print(j1.nom, "a", j1.points, "points et", j2.nom, "a", j2.points, "points")

        elif c1Valeur < c2Valeur:
            print (carte1 + " est plus petit que " + carte2)
            j2.points +=1
            print(j1.nom, "a", j1.points, "points et", j2.nom, "a", j2.points, "points")

    else:
        print("Game Over !")

# Lance la bataille
bataille(0)