import turtle as t
import random

cao = t.Turtle()
t.colormode(255)
cao.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        cao.color(random_color())
        cao.circle(100)
        cao.setheading(cao.heading() + size_of_gap)


draw_spirograph(5)
