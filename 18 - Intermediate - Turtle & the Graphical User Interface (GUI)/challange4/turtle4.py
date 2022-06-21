import turtle as t
import random


cao = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


cao.speed(2)
cao.shape('circle')
cao.pensize(15)

directions = [0, 90, 180, 270]


def moving():
    for _ in range(40):
        cao.forward(20)
        cao.color(random_color())
        cao.setheading(random.choice(directions))


moving()
