from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.level = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"level: {self.level}", align="center",
                   font=FONT)
