# Python_workshop

Resources to perform a workshop based upon Python language -->
Ceci n'est qu'un premier tri des ressources à exploiter, à redéfinir avec Raph.

1. récup de ma veille python: https://docs.google.com/presentation/d/1t_SbXXxjJXkDEJA-YMNQfs_KPddd-xwsnUQDE8viPuA/edit?usp=sharing

2) Caractéristiques du langage (Swinnen - intro)
3) Installation https://www.python.org/downloads/
4) Environnements (terminal ou IDLE: Swinnen p12 et p31)
5) Typage (Swinnen - 16)
6) Flux d'exécution (Swinnen - Chap.3)
7) Blocs d'instructions (Swinnen - 23)
8) Listes (Swinnen - 44)
9) Imports de fonctions (Swinnen - 50)
10) Détente: module Turtle (dessin - Swinnen - 52)
11) Exos de révision (Swinnen - 55)
12) Interfaces graphiques (Swinnen - Chap.8)

##Installation et prérequis

-Vérifiez votre version de Python3 installée (actuellement 3.6+ ou 3.7+)
\$ pyhton3 -V

-Pour installer Python3
\$ sudo apt-get install python3

### IDLE : environnment de développement pour Python

-Installez IDLE :
$ sudo apt-get update
$ sudo apt-get install idle3

-lancez IDLE :
\$ idle

### PyGame

Avant l'installation, assurez-vous d'avoir installé les dépendances : libsdl1.2debian-all (dépôt Universe), libsdl1.2-dev, libsdl-image1.2, libsdl-image1.2-dev, libsdl-ttf2.0-0, libsdl-ttf2.0-dev, libsdl-mixer1.2, libsdl-mixer1.2-dev, libsmpeg0, libsmpeg0-dev, libpng-dev et libjpeg-dev !

Voici la commande pour les installer sous Ubuntu :

\$ sudo apt-get install libsdl1.2debian:i386 libsdl1.2debian

Vous devez avoir pip installé :
$ sudo apt-get install python3-pip

Une fois les dépendances installées, ouvrez un terminal :
$ python3 -m pip install -U pygame --user

Pour tester, lancez le jeu :
$ python3 -m pygame.examples.aliens
