#
# Python:   3.9.5
#
# Author:   Sean Hager
#
# Purpose:  The Tech Academy - Python Course, Polymorphism
#           Demonstrating how to create two classes that inherit from
#           another class.
#           The Parent Class includes one method and each child class
#           has two of their own attributes.
#           Both child classes utilize polymorphism on the parent class method.



# The following example lets car salesman check the information on a car in their lot that a customer
# is looking for. The salesman is looking up a 2021 Nissan Skyline and is prompted with questions to
# see exactly what they are looking for.


# Parent Class Vehicle
class Vehicle:
    make = 'Nissan'
    model = 'Skyline'
    year = 2021

    def getVehicleInfo(self):
        entry_make = input("\nEnter the vehicle make: ")
        entry_model = input("\nEnter the vehicle model: ")
        entry_year = input("\nEnter the vehicle year: ")
        if (entry_make == self.make and entry_model == self.model):
            print("\nThere are currently 20 {} {}s in stock.".format(entry_make,entry_model))
        else:
            print("\nPlease re-enter your request in again, check spelling of query.")

       
# Child Class Color
class colorType(Vehicle):
    car_color = "blue"
    car_coat = "clearcoat"

    def getVehicleInfo(self):
        entry_make = input("\nEnter the vehicle make: ")
        entry_model = input("\nEnter the vehicle model: ")
        entry_color = input("\nEnter the vehicle color: ")
        if (entry_make == self.make and entry_model == self.model and entry_color == self.car_color):
            print("\nThere are currently 20 {} {} {}s in stock.".format(entry_color,entry_make,entry_model))
        else:
            print("\nPlease re-enter your request in again, check spelling of query.")
    
# Child Class Engine
class engineType(Vehicle):
    engineSize = "V6"
    drivetrain = "AWD"

    def getVehicleInfo(self):
        entry_model = input("\nEnter the vehicle model: ")
        entry_engineSize = input("\nEnter the vehicle engine size such as V6: ")
        entry_drivetrain = input("\nEnter the vehicle drivetrain such as AWD for example: ")
        if (entry_model == self.model and entry_engineSize == self.engineSize and entry_drivetrain == self.drivetrain):
            print("\nThere are currently 20 {}s that have an engine size of {} and have {} that are in stock.".format(entry_model,entry_engineSize,entry_drivetrain))
        else:
            print("\nPlease re-enter your request in again, check spelling of query.")



if __name__ == "__main__":
    carStock = Vehicle()
    carStock.getVehicleInfo()

    color = colorType()
    color.getVehicleInfo()

    engine = engineType()
    engine.getVehicleInfo()

    
