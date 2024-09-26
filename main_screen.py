from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

class PingPongGame:
    def __init__(self):
        # Set up the screen
        self.screen = Screen()
        self.screen.title("Ping Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)  # Turn off screen updates to manually refresh

        # Create two paddles
        self.paddle_a = Paddle(-350, 0)  # Left paddle
        self.paddle_b = Paddle(350, 0)   # Right paddle

        # Create the ball
        self.ball = Ball()

        # Create the score
        self.score = Score()

        # Keyboard bindings
        self.screen.listen()
        self.screen.onkeypress(self.paddle_a.move_up, "w")
        self.screen.onkeypress(self.paddle_a.move_down, "s")
        self.screen.onkeypress(self.paddle_b.move_up, "Up")
        self.screen.onkeypress(self.paddle_b.move_down, "Down")

    def run(self):
        while True:
            self.screen.update()  # Refresh the screen
            self.ball.move()      # Move the ball
            self.ball.check_collision_with_paddle(self.paddle_a, self.paddle_b)  # Check paddle collisions
            self.ball.check_out_of_bounds(800, self.score)  # Check for scoring and out of bounds

# Main entry point
if __name__ == "__main__":
    game = PingPongGame()
    game.run()

