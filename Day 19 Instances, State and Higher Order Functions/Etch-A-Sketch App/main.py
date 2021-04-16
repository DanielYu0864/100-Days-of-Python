from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)
def move_backwards():
    timmy.backward(10)
def turn_counter_clockwise():
    timmy.left(5)
def turn_clockwise():
    timmy.right(5)
def clear_drawing():
    timmy.reset()  # Reset all timmy on the Screen to their initial state.
    """
    or timmy.clear() => timmy.penup() => timmy.home() => timmy.pendown()
    """

screen.listen()


screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkey(key='c', fun=clear_drawing)

screen.exitonclick()


