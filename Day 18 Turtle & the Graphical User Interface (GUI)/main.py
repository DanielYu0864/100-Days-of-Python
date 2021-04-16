import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########

'''
# use colorgram.py to get image color
import colorgram  # https://pypi.org/project/colorgram.py/

colors = colorgram.extract('image.png', 30)
rgb_color_list = []
for color in colors:
    color_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])  # color_tuple = (r, g, b)
    rgb_color_list.append(color_tuple)

print(rgb_color_list)
'''

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]


def dot_color():
    timmy_color = random.choice(color_list)
    return timmy_color

def timmy_start_point():
    """reset timmy start point: https://stackoverflow.com/questions/14713037/python-turtle-set-start-position"""
    TURTLE_SIZE = 20
    timmy.penup()
    timmy.goto(TURTLE_SIZE / 2 - screen.window_width() / 3.5, TURTLE_SIZE / 2 - screen.window_height() / 3)
    timmy.pendown()

def timmy_draw():
    """timmy draw 10 * 10 (100) dots"""
    timmy.width(20)  # pen width
    timmy.speed(0)  # timmy speed
    timmy.hideturtle()  # hide timmy
    timmy_start_point()  # reset timmy position
    timmy.penup()  # timmy pen up

    for _ in range(10):
        for _ in range(10):
            """timmy draw dot(size=20, color=dot_color) and move forward 50"""
            timmy.forward(50)
            timmy.dot(20, dot_color())

        """timmy move to upper line every 10 dots"""
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.left(180)


timmy_draw()
screen.exitonclick()
