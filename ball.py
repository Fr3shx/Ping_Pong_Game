from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 1.5  # Horizontal movement speed
        self.dy = 1.5  # Vertical movement speed

    def move(self):
        # Move the ball
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        # Check for top and bottom border collisions
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1  # Reverse vertical direction

        if self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1  # Reverse vertical direction

    def check_collision_with_paddle(self, paddle_a, paddle_b):
        # Paddle collision logic for right paddle
        if (340 < self.xcor() < 350) and (paddle_b.ycor() - 50 < self.ycor() < paddle_b.ycor() + 50):
            self.setx(340)
            self.dx *= -1  # Reverse horizontal direction

        # Paddle collision logic for left paddle
        if (-350 < self.xcor() < -340) and (paddle_a.ycor() - 50 < self.ycor() < paddle_a.ycor() + 50):
            self.setx(-340)
            self.dx *= -1  # Reverse horizontal direction

    def check_out_of_bounds(self, screen_width, score):
        # Check if the ball goes out of bounds (right or left edge)
        if self.xcor() > screen_width / 2:
            self.goto(0, 0)  # Reset ball position
            self.dx *= -1  # Reverse direction
            score.increase_score_a()  # Player A scores

        if self.xcor() < -screen_width / 2:
            self.goto(0, 0)  # Reset ball position
            self.dx *= -1  # Reverse direction
            score.increase_score_b()  # Player B scores
            

