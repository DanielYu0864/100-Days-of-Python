from turtle import Turtle, Screen
import heroes  # more about heroes: https://pypi.org/project/heroes/
screen = Screen()

print(heroes.gen())

# from turtle import * (* means everything here)
'''
# turtle doc: https://docs.python.org/3/library/turtle.html
(GUI) -> Graphical Uer Interface

* shift + F6 -> to refactor the variable name

if only user once -> import turtle, timmy = turtle.Turtle()
if more -> from turtle import Turtle, timmy = Turtle(), tom = Turtle()

# Tuple in python:
    my_tuple = (1, 2, 3)
    py_tuple[1] // 2
    *! the value inside of tuple can not change 

# Aliasing Modules
-----------------------------------------------
key word | Module name | key word |  alias name
-----------------------------------------------
 import  |    turtle   |    as    |      t
-----------------------------------------------
import turtle as t -> assign turtle to t
timmy = t.Turtle() -> equal to turtle.Turtle()

# Installing Modules
pypi.org => https://pypi.org/

'''

timmy = Turtle()
timmy.shape('turtle')
timmy.color('chartreuse4', 'DarkOliveGreen')


# use timmy to draw a square
def draw_square():
    for _ in range(4):
        timmy.right(90)
        timmy.fd(100)


# timmy draw a dashed line
def draw_dash():
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()  # Pull the pen up – no drawing when moving.
        timmy.forward(10)
        timmy.pendown()  # Pull the pen down – drawing when moving.


# timmy draw nth shapes
def draw_n_shapes(num_sides):
    """ get shapes deg by 360 / nth of sides """
    deg = 360 / num_sides
    for _ in range(num_sides):
        timmy.right(deg)
        timmy.forward(100)


import random


def random_pen_color():
    """
    use Hex Color Code to get random color: https://stackoverflow.com/questions/28999287/generate-random-colors-rgb
    """
    # random_color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    # timmy.pencolor(random_color)

    '''
    use tuple to create random RGB color
    '''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    screen.colormode(255)
    timmy.color(random_color)




# draw from triangle to decagon:
# for i in range(3, 11):
#     random_pen_color()
#     draw_n_shapes(i)


# timmy Draw a Random Walk
def draw_random_walk():
    timmy.pensize(10)
    timmy.forward(30)

    turn_left_or_right()
    random_pen_color()


def turn_left_or_right():
    random_int = random.randint(0, 4)
    timmy.setheading(90 * random_int)


timmy.speed(0)  # https://docs.python.org/3/library/turtle.html?highlight=speed#turtle.speed

# random walk for 100 times
# for _ in range(100):
#     draw_random_walk()

# timmy make a spirograph
def make_spirograph(deg):
    for _ in range(int(360 / deg)):
        random_pen_color()
        timmy.circle(100)
        timmy.left(deg)

make_spirograph(5)



screen.exitonclick()
