# Un premier petit exercice consiste à coder un jeu de "Pierre-Papier-Ciseaux"

# Son intérêt est de se familiariser avec la syntaxe de Python

# ATTENTION : l'instruction "SWITCH", n'existe pas dans Python: il faut utiliser if - (elif) - else

##################################################### UNE SOLUTION EST PROPOSEE FIN DE FICHIER

#  ------------------------ >  LET's GO :-)

# Import du module "random"



# inviter l'utilisateur avec la fonction input() --> (réponses acceptées: O - N ) et gérer son refus de jouer


# gérer le mauvais choix de validation acceptation


# si le jeu est accepté, vérifier que la proposition du joueur correspond bien à pierre, papier ou ciseaux avec "while not ()"


    # génerer aléatoirement un ppc de l'AI avec la fonction randint() et ensuite if-elif-else


    # gérer l'égalité et comparer l'entrée et le choix AI


    # --------------------------------------------------------- SOLUTION PROPOSÉEE ---->












    

# Import du module "random"

from random import *

# inviter l'utilisateur avec la fonction input() --> (réponses acceptées: O - N ) et gérer son refus de jouer
game = ""
game = input('Voulez-vous jouer à Pierre-Papier-Ciseaux ? \nEntrez "O" ou "N".')

# gérer le mauvais choix de validation acceptation
while not (game == "O" or game == "N"):
    print('Veuillez entrer "O" ou "N".')
    game = input('Voulez-vous jouer à Pierre-Papier-Ciseaux ? \nEntrez "O" ou "N".')

# si le jeu est accepté, vérifier que la proposition du joueur correspond bien à pierre, papier ou ciseaux avec "while not ()"
if (game == "O"):
    choixUt=""
    while not (choixUt=="pierre" or choixUt=="papier" or choixUt=="ciseaux"):
        choixUt = input("Faites votre choix entre pierre, papier et ciseaux : ")

    # génerer aléatoirement un ppc de l'AI avec la fonction randint() et ensuite if-elif-else
    x = randint (1,3)
    choixAI = ""
    if (x==1):
        choixAI = "pierre"
    elif (x==2):
        choixAI = "papier"
    else:
        choixAI = "ciseaux"

    # gérer l'égalité et comparer l'entrée et le choix AI
    if (choixUt == choixAI):
        print("Egalité")
    else: 
        if (choixUt == "pierre"):
            if (choixAI == "papier"):
                print('L\'AI a choisi "papier", vous avez perdu')
            else:
                print('L\'AI a choisi "ciseaux", vous avez gagné')
        if (choixUt == "papier"):
            if (choixAI == "pierre"):
                print('L\'AI a choisi "pierre", vous avez gagné')
            else:
                print('L\'AI a choisi "ciseaux", vous avez perdu')
        if (choixUt == "ciseaux"):
            if(choixAI == "pierre"):
                print('L\'AI a choisi "ciseaux", vous avez gagné')
            else:
                print('L\'AI a choisi "papier", vous avez perdu')
else: 
    print("Ce sera pour une autre fois alors !\nA bientôt")