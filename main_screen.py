from turtle import Screen
from paddle import Paddle


# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pong Game")
screen.tracer(0)

# Create paddles
left_paddle = Paddle(-370, 0)  # Left paddle
right_paddle = Paddle(370, 0)   # Right paddle

# Set up key bindings
screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up2, 'Up')
screen.onkey(right_paddle.down2, 'Down')

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()



# Exit on click
screen.exitonclick()
