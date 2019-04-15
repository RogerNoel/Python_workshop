#proposer une autre partie

from random import *

#inviter l'utilisateur
game = ""
game = input('Voulez-vous jouer à Pierre-Papier-Ciseaux ? \nEntrez "O" ou "N".')
print(game)
#gérer le mauvais choix de validation acceptation
while not (game == "O" or game=="N"):
    print('Veuillez entrer "O" ou "N".')
    game = input('Voulez-vous jouer à Pierre-Papier-Ciseaux ? \nEntrez "O" ou "N".')

if (game == "O"):
    choixUt=""
    while not (choixUt=="pierre" or choixUt=="papier" or choixUt=="ciseaux"): #gérer les mauvaises entrées utilisateurs
        choixUt = input("Faites votre choix entre pierre, papier et ciseaux : ")
    #génerer aléatoirement un ppc de l'AI
    x = randint (1,3)
    AIChoice = ""
    if (x==1):
        AIChoice = "pierre"
    elif (x==2):
        AIChoice = "papier"
    else:
        AIChoice = "ciseaux"

    #gérer l'égalité
    if (choixUt == AIChoice):
        print("Egalité")
    else: #comparer l'entrée et le choix AI
        if (choixUt == "pierre"):
            if (AIChoice == "papier"):
                print('L\'AI a choisi "papier", vous avez perdu')
            else:
                print('L\'AI a choisi "ciseaux", vous avez gagné')
        if (choixUt == "papier"):
            if (AIChoice == "pierre"):
                print('L\'AI a choisi "pierre", vous avez gagné')
            else:
                print('L\'AI a choisi "ciseaux", vous avez perdu')
        if (choixUt == "ciseaux"):
            if(AIChoice == "pierre"):
                print('L\'AI a choisi "ciseaux", vous avez gagné')
            else:
                print('L\'AI a choisi "papier", vous avez perdu')
else: #gérer le refus utilisateur
    print("Ce sera pour une autre fois alors !\A bientôt")





