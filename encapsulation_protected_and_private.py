#
# Python:   3.9.5
#
# Author:   Sean Hager
#
# Purpose:  The Tech Academy - Python Course, Encapsulation
#
#          In this assignment, I am creating a class that utilizes
#          encapsulation. The class makes use of private and protected
#          attribute or function. The program then creates an object that makes
#          use of protected and private




class myProtectedVar:
    def __init__(self):
        self._protectedVar = 0


class Protected:
    def __init__(self):
        self.__privateVar = 25
    def getPrivate(self):
        print(self.__privateVar)
    def setPrivate(self, private):
        self.__privateVar = private
    



if __name__ == "__main__":
    obj = myProtectedVar
    obj._protectedVar = 105
    print(obj._protectedVar)

    obj2 = Protected()
    obj2.getPrivate()
   
