from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)

    def up2(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down2(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)