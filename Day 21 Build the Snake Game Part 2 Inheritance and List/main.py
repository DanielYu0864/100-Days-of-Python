from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time  # https://docs.python.org/3/library/time.html?highlight=time#module-time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')  # https://docs.python.org/3/library/turtle.html?highlight=title#turtle.title
screen.tracer(0)  # https://docs.python.org/3/library/turtle.html?highlight=tracer#turtle.tracer

# step 1 Create a snake body
snake = Snake()


# step 4 Detect collision with food
food = Food()

# step 5 Create a scoreboard
scoreboard = Scoreboard()

# step 3 Control the snake
screen.listen()  # https://docs.python.org/3/library/turtle.html?highlight=turtle%20listen#turtle.listen
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


# step 2 Move the snake

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)  # https://docs.python.org/3/library/time.html?highlight=time%20sleep#time.sleep
    snake.move()
    # step 4 Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # step 7 Detect collision with tail
        snake.extend()
        # step 5 Create a scoreboard
        scoreboard.update_score()

    # step 6 Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # step 7 Detect collision with tail
    """
    # python Slicing: https://dev.to/duomly/what-is-slicing-in-python-58f2#:~:text=Slicing%20in%20Python%20is%20a,Pandas%20series%20and%20data%20frames.
    
    EX:
    piano_keys = [a, b, c, d, e, f, g]
                |  |  |  |  |  |  |  |
                0  1  2  3  4  5  6  7
    piano_keys[2:5] -> return the slicing it from position 2 to position 5 => [c, d, e]
    piano_keys[2:] -> return the slicing it from index 2 to the end => [c, d, e, f, g]
    piano_keys[:5] -> return the slicing it from start to the index 5 => [a, b, c, d, e]
    piano_keys[2:5:2] -> return the slicing it from position 2 to position 5 every 2 items => [c, e]
    piano_keys[::2] -> return the slicing while list by every 2 items => [a, c, e, g]
    piano_keys[::-1] -> return the reverse while list => [g, f, e, d, c, b, a]
    
    * also works on tuple
    """
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()


# TODO: step 1 create a snake body
# TODO: step 2 move the snake
# TODO: step 3 control the snake
# TODO: step 4 detect collision with food
# TODO: step 5 create a scoreboard
# TODO: step 6 detect collision with wall
# TODO: step 7 detect collision with tail

