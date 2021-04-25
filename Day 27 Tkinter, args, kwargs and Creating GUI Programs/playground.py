"""Example for *args"""


def add(*args):
    arg_sum = 0
    for n in args:
        arg_sum += n

    return arg_sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    #
    # print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw): # https://stackoverflow.com/questions/1098549/proper-way-to-use-kwargs-in-python
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)