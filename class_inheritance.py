#
# Python:   3.9.5
#
# Author:   Sean Hager
#
# Purpose:  The Tech Academy - Python Course, Demonstrating Class Inheritance
#           In the following code, I am demonstrating how to create a parent class with
#           two child classes with their own added attributes.



class Vehicle:
    make = 'Nissan'
    model = 'Skyline'
    color = 'Blue'
    year = 2021

class Horsepower(Vehicle):
    horsepower_number = 600
    rpm = 6800

class Engine(Vehicle):
    engine_size = 'turbocharged V6'
    drivetrain = 'AWD'






if __name__ == "__main__":
    start()
