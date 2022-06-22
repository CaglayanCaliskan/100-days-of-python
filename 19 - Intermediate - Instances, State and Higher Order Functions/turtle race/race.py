from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
w = 500
h = 400
screen.setup(w, h)
user_bet = screen.textinput(
    title="Make your bet ", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

pos_x = -240
pos_y = -80
for i in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape('turtle')
    new_turtle.color(colors[i])
    new_turtle.goto(pos_x, pos_y)
    all_turtles.append(new_turtle)
    pos_y += 40
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:

                screen.textinput(title="result",
                                 prompt=f"you Winnn ! winner is *** {winning_color} *** ")
            else:
                screen.textinput(title="result",
                                 prompt=f"You have lost ! the winner s*** {winning_color} ***")

            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

print(all_turtles)
screen.exitonclick()
