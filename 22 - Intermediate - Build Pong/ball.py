from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    # def go_up(self):
    #     new_y = self.ycor() + 20
    #     self.goto(self.xcor(), new_y)

    # def go_down(self):
    #     new_y = self.ycor() - 20
    #     self.goto(self.xcor(), new_y)
