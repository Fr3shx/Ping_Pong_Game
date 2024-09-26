import turtle

class Score:
    def __init__(self):
        self.score_a = 0
        self.score_b = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.pen.clear()
        self.pen.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align="center", font=("Courier", 24, "normal"))

    def increase_score_a(self):
        self.score_a += 1
        self.update_score()

    def increase_score_b(self):
        self.score_b += 1
        self.update_score()
