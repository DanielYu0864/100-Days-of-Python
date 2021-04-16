import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
# .setup(width, height, startx, starty): https://docs.python.org/3/library/turtle.html?highlight=setup#turtle.setup
user_bet = screen.textinput(title="Make your bet", prompt="Which timmy will win the race? Enter a color: ")
# .textinput(title, prompt) -> return a string : https://docs.python.org/3/library/turtle.html?highlight=textinput#turtle.textinput

rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen.colormode(1)
position = -150
all_timmies = []

for color in rainbow_color:
    timmy = Turtle(shape='turtle')  # timmy width and height = 40 * 40
    timmy.color(color)
    timmy.penup()
    timmy.goto(x=-230, y=position)  # https://docs.python.org/3/library/turtle.html?highlight=goto#turtle.goto
    position += 60
    all_timmies.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:

    for timmy in all_timmies:
        if timmy.xcor() > 230:  # xcor() https://docs.python.org/3/library/turtle.html?highlight=xcor#turtle.xcor
            is_race_on = False
            winning_color = timmy.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} timmy is the winner!")
            else:
                print(f"You've lost! The {winning_color} timmy is the winner!")

        rand_distance = random.randint(0, 10)
        timmy.forward(rand_distance)




screen.exitonclick()