from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.left(90)
        self.reset()

    def go_up(self):
        self.forward(MOVE_DISTANCE * 2)
        self.crossing_control()

    def reset(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def crossing_control(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
