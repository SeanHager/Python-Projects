#
# Python:   3.9.5
#
# Author:   Sean Hager
#
# Purpose:  The Tech Academy - Python Course, Demonstrating Python and HTML Integration
#           Script creates a simple GUI that allows the user to input text and initiate the web page
#           generation process.
#
#           Script generates a web page that sets the user’s input as the body text for the web page.
#
#           Script then opens the generated web page in the browser.


#Import tkinter all modules and import webbrowser module.
#webbrowser is needed in working with html and python scripts
from tkinter import *
import webbrowser

#define wbGui as Tk() variable to create window
wbGui = Tk()
#define source as a string variable for user text entry. fetches the variable
source = StringVar()
#define window size and window title
wbGui.geometry('450x250+500+300')
wbGui.title('Web Python Challenge')

#define variable webBrowser to handle script
def webBrowser():
    #define a variable for webBrowser to open and write a new window
    file = open('index.html', 'w')
    #define a variable named text to store the string variable
    text = source.get()
    #write in user message, %s holds string for webpage
    message = "<html><head></head><body><h1>%s</h1></body></html>" %text
    #writes user message onto screen
    file.write(message)
    #closes script
    file.close()
    #opens new index.html save file to display text
    webbrowser.open_new_tab('index.html')

#Create label widget with text and place on grid
wblabel = Label(wbGui,text='Enter into the webpage your text! Change it from\n'
                'Stay tuned for our amazing summer sale can be changed!')
wblabel.grid(row=0, column=1, padx=80, pady=10)

#Create user entry widget to allow user to enter text needed
wbEntry = Entry(wbGui,textvariable=source)
wbEntry.grid(row=2, column=1, columnspan=3, padx=120, pady=10)

#Create button to submit user input and open new browser window with supplied string
wbbutton = Button(wbGui,text="Open Browser", width=10, height=2, command = webBrowser)
wbbutton.grid(row=4, column=1, padx=120, pady=10)



