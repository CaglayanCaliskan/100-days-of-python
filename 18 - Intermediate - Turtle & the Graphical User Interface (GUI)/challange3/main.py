
from time import sleep
from turtle import Screen, Turtle
import random


cao_turtle = Turtle()
colors = ['red', 'brown', 'blue', 'orange']
print(random.choice(colors))


cao_turtle.speed(2)


def cizim(kenar, adet):
    for n in range(adet):
        for _ in range(kenar):
            cao_turtle.forward(100)
            cao_turtle.right(360 / kenar)
        kenar = kenar + 1
        renk = random.choice(colors)
        cao_turtle.color(renk)
        cao_turtle.pencolor(renk)


cizim(3, 5)


screen = Screen()
screen.exitonclick()
