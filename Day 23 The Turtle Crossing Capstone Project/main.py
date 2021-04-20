import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
car_manager = CarManager()
timmy = Player()
screen.listen()
screen.onkeypress(timmy.move, 'Up')  # Move the turtle with keypress
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()  # Create and move the cars
    car_manager.move()

    for car in car_manager.all_cars:  # Detect collision with car
        if timmy.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

    if timmy.ycor() > 280:  # Detect when turtle reaches the other side
        timmy.reset_player()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()

# todo: Move the turtle with keypress
# todo: Create and move the cars
# todo: Detect collision with car
# todo: Detect when turtle reaches the other side
# todo: Create a scoreboard
