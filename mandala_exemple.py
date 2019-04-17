from turtle import *
from random import *

speed('fastest')

number_of_colors = 50

colors = ["#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]

def spirale(rayon=1, rayonSpiral=500):
    while(rayon < rayonSpiral): 
        circle(rayon, 180)
        rayon += 5  
        
    rayon = 1

def squaredRound(col, lg):
    for i in range(90):
        color(col)
        forward(lg)
        left(91)

def forme3(col, lg):
    for i in range(75):
        color(col)
        forward(lg)
        left(115)

for i in range(number_of_colors):
    color(choice(colors))
    spirale(randint(2,5), randint(75,500))
    up()
    goto(randint(-500,500),randint(-500,500))
    down()
    squaredRound(choice(colors), randint(75,500))
    up()
    goto(randint(-500,500),randint(-500,500))
    down()
    forme3(choice(colors), randint(50,500))

done()

