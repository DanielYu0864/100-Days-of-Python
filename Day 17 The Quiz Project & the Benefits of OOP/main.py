"""
# class in python =>
obj | class
car = CarBlueprint()

* name of class: CarCamshaftPulley -> every word start uppercase (PascalCase)
* method in class -> always need 'self' parameter as a first parameter EX: def method(self):

# constructor (initialize an object)  in python object =>
class Car:
    def __init__(self):
    #initialise attributes


# Attribute in python object =>
class Car:
    def __init__(self, seats):
        self.seats = seats


# Method (function) in python object =>
class Car:
    def enter_race_mode(self):
        self.seats = 2

* call method -> my_car.enter_race_mode()
"""


class User:
    # pass
    # more about pass: https://www.programiz.com/python-programming/pass-statement#:~:text=In%20Python%20programming%2C%20the%20pass,in%20no%20operation%20(NOP).

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """
        A is following B, B get a follower
        => A.following + 1, B.follower + 1
        """
        user.followers += 1
        self.following += 1


user_1 = User('001', 'daniel')
user_2 = User('002', 'linda')

user_1.follow(user_2)




