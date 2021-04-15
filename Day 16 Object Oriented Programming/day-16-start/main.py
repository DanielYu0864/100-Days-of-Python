# import another_module
#
# print(another_module.another_variable)

'''
# object class
obj | Class
car = CarBlueprint()
'''
'''
# Object Methods
obj|Method
car.stop()
'''
'''
# object attributes
obj|attributes
car.speed
'''

'''
from turtle import Turtle, Screen
# more about turtle: https://docs.python.org/3/library/turtle.html
timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('SkyBlue2') # more about turtle.color(): https://cs111.wellesley.edu/labs/lab01/colors
timmy.forward(100) # more about turtle.forward(): https://docs.python.org/3/library/turtle.html#turtle.forward

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
'''


# Python packages: https://pypi.org/
from prettytable import PrettyTable
# more about prettytable: https://pypi.org/project/prettytable/
# prettytable tutorial: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
print(table.align)
table.align = 'l'  # .align = attributes 'l' = left
print(table.align)
print(table)

