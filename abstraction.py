#
# Python:   3.9.5
#
# Author:   Sean Hager
#
# Purpose:  The Tech Academy - Python Course, Abstraction
#
#          In this assignment, I am creating a class that utilizes
#          abstraction. The class contains one abstract and one regular method.
#          The program creates a child class that defines the implementation
#          of its parents abstract method.
#          The program then creates an object that utilizes both the parent and
#          child methods.


from abc import ABC, abstractmethod
class fruit(ABC):
    def yourReceipt(self, amount):
        print("Your total purchase amount of fruit comes to: ",amount)
    @abstractmethod
    def totalPayment(self, amount):
        pass

class customerPayment(fruit):
    def totalPayment(self, amount):
        print("You have purchased more than {} of fruit from our stand. Thank you!".format(amount))
        



if __name__ == "__main__":
    obj = customerPayment()
    obj.yourReceipt("$50")
    obj.totalPayment("$50")
    
