## Ceci est un script pour jouer à la bataille
## Codé par Raphaël Colson en janvier 2019

from random import *

##Initiation des dictionnaires avec les valeurs des cartes pour la bataille
listeCouleurs = ["♠", "♥", "♦", "♣"]
listeRangs = {
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
carte1 = ""
carte2 = ""
apresEgalite = False

#Constructeur de carte
class Carte:
    """Classe de cartes"""
    def __init__(self, couleur, rang):
        self.nom = "{0} de {1}".format(rang, couleur)

#Constructeur d'un jeu de carte
class Jeu:
    """Classe du jeu de cartes"""
    def __init__(self):
        self.jeu = {}
        self.listeDuJeu = []
        for couleur in listeCouleurs: 
            for cleRang, valeurRang in listeRangs.items():
                rang = cleRang
                valeur = valeurRang
                carte = Carte(couleur, rang)
                self.jeu[carte.nom] = valeur
                self.listeDuJeu.append(carte.nom)

    def afficherJeu(self):
        """Afficher le jeu construit"""
        print(self.jeu)

    def battre(self):
        """Mélanger le jeu"""
        shuffle(self.listeDuJeu)

    def tirerJeu(self):
        """Tirer les cartes du jeu une à une"""
        i = 0
        while i < 52:
            print(self.listeDuJeu[i])
            i += 1
    
    def tirerCartesAuHasard(self, nbr):
        """Tirer une carte au hasard"""
        i = 1
        while i <= nbr:
            r = randint(0,51)
            print(self.listeDuJeu[r])
            i += 1

    def tirerCarte(self, n):
        """Tirer la carte suivante"""
        return self.listeDuJeu[n]

#Constructeur d'un joueur et de son jeu
class Joueur(Jeu):
    """Classe des joueurs"""
    def __init__(self, nom):
        Jeu.__init__(self)
        self.nom = nom
        self.points = 0

def askName():
    """Demander le nom du premier joueur et construire son jeu"""
    reply = str(input("Quel est votre nom ? "))
    global j1
    j1 = Joueur(reply)

def gagne(joueur):
    """Afficher le gagnant"""
    print (joueur.nom +" a gagné,\n")
    print ("{0} a {1} point(s) et {2} a {3} point(s)".format(j1.nom, j1.points, j2.nom, j2.points))

def batailleSuite(n):
    confirm = yes_or_no("\nOn continue ?")
    if confirm:
        bataille(n+1)

def egalite(n):
    print("2 points en suspend")
    bataille(n+1)

def bataille(n):
    """Lancer la bataille entre 2 cartes"""
    if(n < 52):
        global apresEgalite
        carte1 = j1.tirerCarte(n)
        c1Valeur = j1.jeu[carte1]
        carte2 = j2.tirerCarte(n)
        c2Valeur = j2.jeu[carte2]
        print("\n{0}, votre carte est : {1}".format(j1.nom, carte1))
        print("La carte de {0} est : {1}".format(j2.nom, carte2))
        if c1Valeur > c2Valeur:
            print ("\n" + carte1 + " est plus grand que " + carte2)
            if apresEgalite:
                j1.points += 3
                apresEgalite = False
            else:
                j1.points +=1
            gagne(j1)
            batailleSuite(n)

        elif c1Valeur < c2Valeur:
            print (carte1 + " est plus petit que " + carte2)
            if apresEgalite:
                j2.points += 3
                apresEgalite = False
            else:
                j2.points +=1
            gagne(j2)
            batailleSuite(n)

        else:
            print ("!!! egalite !!!")
            apresEgalite = True
            egalite(n)
    else:
        print("Game Over !")

def yes_or_no(question):
    """Demander une confirmation"""
    reply = str(input(question+' (o/n): ')).lower().strip()
    if reply[0] == 'o':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Oh lalala... il me faut un oui ou non ")

#Lancement du script pour jouer une partie de bataille
askName()
j2 = Joueur("Ordi")
j1.battre()
j2.battre()
confirm = yes_or_no("{0}, voulez-vous jouer ?".format(j1.nom))

if confirm:
    bataille(0)

