from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)  # Paddle size
        self.penup()
        self.goto(x_pos, y_pos)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:  # Limit paddle movement within the screen bounds
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -240:  # Limit paddle movement within the screen bounds
            self.goto(self.xcor(), new_y)



