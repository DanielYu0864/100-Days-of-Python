from turtle import Turtle, Screen
'''
# event listener in turtle: https://docs.python.org/3/library/turtle.html#turtle.listen
'''
timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

"""
Keyword Argument
def my_function(a,b,c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    
EX: my_function(1,2,3)
"""
"""
Positional Argument
def my_function(a,b,c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
EX: my_function(a=1,b=2,c=3)
"""