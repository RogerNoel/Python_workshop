# On va faire un jeu de cartes en utilisant la POO 

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

# On crée une classe pour créer une carte :

class Carte:
    ...

# Crée une instance de carte et informe du nom de la carte et de sa valeur
...




# On va créer une classe Jeu qui va boucler la liste des couleurs et le dictionnaire des rangs pour construire un jeu de 52 cartes
# Cette classe va comporter un dictionnaire pour associer les valeurs à chaque nom de carte, ex. Valet de trefle : 11
# Cette classe va aussi comporter une liste de toutes les cartes qui nous servira à mélanger le jeu de cartes

















 # On peut créer une instance de Jeu et afficher le jeu pour vérifier s'il est bien construit  




# Ajoute ensuite une fonction pour mélanger le jeu à la classe Jeu, n'oublie pas d'importer la librairie random


# Toujours dans la classe Jeu, Ajoute maintenant une fonction qui prendra en paramètre un index de la listeDuJeu pour tirer une carte dans le jeu mélangé et teste-là



# Voilà, nous allons pouvoir commencer la bataille ! Crée une fonction qui lancera une battaille entre 2 joueurs, pour cela il te faudra une classe Joueur pour créer un joueur qui dépendra de la classe Jeu. Cette classe Joueur aura 2 propriétés : un nom de joueur (passé en paramètre) et un total de points. 

 





# On peut donc créer 2 joueurs et afficher leurs noms et leurs points :
j1 = ...
j2 = ...
print(...)

# Comme elle dépend de Jeu, elle héritera aussi de ses caractéristiques. Utilise la fonction pour mélanger le jeu de joueur1, affiche le jeu mélangé et affiche une carte tiré avec l'index 0 : 




# Crée la fonction pour la bataille, ici je te laisse réfléchir à l'algorithmie... 




















# Lance la bataille
