# On va faire un jeu utilisant la POO 

# On crée une classe pour un  personnage

class Perso:
    def __init__ (self, nom, vie = 50, force = 10):
        self.nom = nom
        self.vie = vie
        self.force = force

Luke = Perso("Luke", 30, 20)

print(Luke.nom + "a" + Luke.vie + "de points de vie")