#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((1200, 800))

# création du fond
fond = pygame.image.load("background.jpg").convert() #convertit au bon format, ce qui rendra l'affichage plus rapide ! 
fenetre.blit(fond, (0,0)) # il faut coller l'image sur le fond en pos x et y

# création du vaisseau
vaisseau = pygame.image.load("spaceship.png").convert_alpha()
fenetre.blit(vaisseau, (100,100))

#Rafraîchissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle

