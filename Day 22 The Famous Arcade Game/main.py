"""
class main
class scoreboard
class middle line
class ball
class paddle
"""
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# step 1 Create the screen -> height = 600, width = 800, background_color = "black"
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)  # turn of the animation

# step 2 Create and move a paddle
# step 3 Create anther paddle
# step 4 Create the ball and make it move
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")



game_on = True
while game_on:
    time.sleep(ball.move_speed)  # ball.move_speed second gap between every while loop
    screen.update()
    ball.move()

    # step 5 Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # step 6 Detect collision With paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # step 7 Detect when paddle misses
    # step 8 Keep score
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()

# todo: step 1 Create the screen -> height = 600, width = 800, background_color = "black"
# todo: step 2 Create and move a paddle
# todo: step 3 Create anther paddle
# todo: step 4 Create the ball and make it move
# todo: step 5 Detect collision with wall and bounce
# todo: step 6 Detect collision With paddle
# todo: step 7 Detect when paddle misses
# todo: step 8 Keep score
