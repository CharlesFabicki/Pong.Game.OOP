from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
print(f"Welcome to Pong Game written in Python.\n"
      f"Use 'w', 's' key to play with left paddle and 'up arrow', 'down arrow' to play with right paddle. Enjoy the Game !")
screen = Screen()
screen.bgcolor("blue")
screen.setup(width=1000, height=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    # Check if the ball hits the wall then bounce from it
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    # Check if the ball hits the paddle then bounce
    if ball.distance(r_paddle) < 30 and ball.xcor() > 430 or ball.distance(l_paddle) < 30 and ball.xcor() < -430:
        ball.bounce_x()
    # Check if right paddle misses
    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.l_point()
    # Check if left paddle misses
    if ball.xcor() < -480:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
