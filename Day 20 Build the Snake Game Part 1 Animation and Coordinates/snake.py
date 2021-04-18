from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):  # step 1 Create a snake body

        for p in STARTING_POSITIONS:
            timmy = Turtle(shape='square')
            timmy.color('white')
            timmy.penup()
            timmy.goto(p)
            self.segments.append(timmy)

    def move(self):  # step 2 Move the snake

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()  # return the timmy's x coordinate
            new_y = self.segments[i - 1].ycor()  # return the timmy's y coordinate
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # step 3 Control the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)