from turtle import Screen, Turtle
from snake import Snake
import time  # https://docs.python.org/3/library/time.html?highlight=time#module-time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')  # https://docs.python.org/3/library/turtle.html?highlight=title#turtle.title
screen.tracer(0)  # https://docs.python.org/3/library/turtle.html?highlight=tracer#turtle.tracer

# step 1 Create a snake body

snake = Snake()

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


'''

'''


screen.exitonclick()
