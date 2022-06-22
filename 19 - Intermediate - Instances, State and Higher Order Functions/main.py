
from turtle import Turtle, Screen
import keyword
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def move_back():
    tim.backward(10)


def game_reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_back, "Down")
screen.onkey(game_reset, "c")

screen.exitonclick()
