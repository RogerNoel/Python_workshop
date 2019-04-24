from turtle import *
from random import *

speed('fastest')

number_of_colors = 15

colors = ["#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
          for i in range(number_of_colors)]


def spirale():
    rayon = randint(2, 5)
    rayonSpiral = randint(75, 500)
    while(rayon < rayonSpiral):
        circle(rayon, 180)
        rayon += 5

    rayon = 1


def squaredRound():
    fw = randint(75, 500)
    for i in range(90):
        forward(fw)
        right(91)


def triangle():
    fw = randint(50, 500)
    for i in range(75):
        forward(fw)
        right(115)


def pyramid():
    distance = 5
    while distance < randint(500, 1200):
        forward(distance)
        right(90)
        distance += randint(4, 8)


def web():
    distance = randint(1, 5)
    while distance < randint(500, 1200):
        left(52)
        forward(distance)
        distance += 3


def sphere():
    size = randint(75, 500)
    for i in range(36):
        color(choice(colors))
        circle(size)
        left(10)


def move(x, y):
    up()
    goto(x, y)
    down()


listOfShapes = [
    "spirale()",
    "squaredRound()",
    "triangle()",
    "pyramid()",
    "web()",
    "sphere()"
]

screen = Screen()

def nextDraw(x,y):
    draw(x,y)


def draw(x, y):
    screen.onclick(None)    
    move(x, y)
    color(choice(colors))
    eval(choice(listOfShapes))
    screen.onclick(nextDraw)
   

draw(0,0)

done()