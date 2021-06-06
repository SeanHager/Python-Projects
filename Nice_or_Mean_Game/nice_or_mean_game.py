#
# Python:   3.9.5
#
# Author:   Sean Hager
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together
#           Demonstrating how to pass variabels from function to function
#           while producing a game.
#
#           Remember, function_name(variable) means that we pass in the variable.
#           return variable means that we are returning the variable to
#           back to the calling function. 


# Add image to Python game
from PIL import Image

img = Image.open('C:/Users/Seanbon/Desktop/Tech Academy/Python/Nice_or_Mean_Game/nice_mean.jpg')
img.show()

# Game coding begin

def start(nice=0,mean=0,name=""): # name will receive default empty value of ""
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    

def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name.
    if name != "": #if name isn't empty, print the following
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True #if name is empty, do the following else statement
        while stop:
            if name == "": #if name is empty
                name = input("\nWhat is your name? \n>>> ").capitalize() #capitalize is built in method
                if name != "": #if name is not empty
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False #take boolean value False shuts off block of code now that we have users name, we do not need to keep checking name
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower() #lower will make user choice of n or m lower to coincide with our loop.
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1) # 0 + 1 gets plugged into nice
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1) # 0 + 1 gets plugged into mean
            stop = False
    score(nice,mean,name) #pass the 3 variables to score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))
    
    
def score (nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if the condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if the condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them, else loop through nice_mean loop above
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # Substitute the {} wild cards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))  
    # call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    # Substitute the {} wild cards with our variable values
    print("\nAhhh to bad {}, game over! \nYou live in a dirty beat-up van by the river, \nwretched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play with
    start(nice,mean,name)



# Game coding end




# Initialize game
if __name__ == "__main__":
    start()
