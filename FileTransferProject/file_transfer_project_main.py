#
# Python:   3.9.5
#
# Author:   Sean Hager
#
# Purpose:  The Tech Academy - Python Course, Demonstrating Python File Transfer. 
#           Created a simple GUI that allows the user to do the following:
#
#           1. Allow the user to browse and choose a specific folder that will contain
#           the files to be checked daily.
#           2. Allow the user to browse and choose a specific folder that will receive
#           the copied files.
#           3. Allow the user to manually initiate the 'file check' process that is
#           performed by the script.
#
#           GUI can copy same files over to seperate destination folder as well as
#           move the files completely.
#
#           Utilze FolderA and FolderB, with FolderA containing basic .txt files to move
#
#           NOTE: Script is base project for adding features in the future such as warning
#           user if fields are empty.

#importing all required modules, utilizing shutil to complete file transfer in the GUI
import shutil
import os, time
import datetime
import datetime as dt
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from os import walk

     
# Defining Widgets() function to
# create necessary tkinter widgets such as label, input boxes, and buttons
def Widgets():
    # Label 'Copy' Widget
    link_Label = Label(root, text ="Choose Folder Containing Files : ",bg = "white")
    link_Label.grid(row = 1, column = 0,pady = 5, padx = 5)
    # Entry Widget for Source
    root.sourceText = Entry(root, width = 50, textvariable = sourceLocation)
    root.sourceText.grid(row = 1, column = 1, pady = 5, padx = 5, columnspan = 2)
    # Source button to enable user browsing
    source_browseButton = Button(root, text ="Browse",command = SourceBrowse, width = 15)
    source_browseButton.grid(row = 1, column = 3, pady = 5, padx = 5)
    # Label 'Destination' Widget
    destinationLabel = Label(root, text ="Select The Destination : ", bg ="white")
    destinationLabel.grid(row = 2, column = 0, pady = 5, padx = 5)
    # Entry Widget for Destination
    root.destinationText = Entry(root, width = 50,textvariable = destinationLocation)
    root.destinationText.grid(row = 2, column = 1,pady = 5, padx = 5,columnspan = 2)
    # Browse button to enable user browsing
    dest_browseButton = Button(root, text ="Browse",command = DestinationBrowse, width = 15)
    dest_browseButton.grid(row = 2, column = 3,pady = 5, padx = 5)
    # File check button that enables user to click to move files over if edited within 24 hours.
    fileCheckButton = Button(root, text ="Auto File Transfer",command = FileCheck, width = 15)
    fileCheckButton.grid(row = 3, column = 1,pady = 5, padx = 5)

 
def SourceBrowse():
    #obtain folder choice from user and store in a variable named sourceDirectory
    sourceDirectory = filedialog.askdirectory(initialdir='FolderA')
     
    # Displaying the selected files in the root.sourceText
    # Entry using root.sourceText.insert()
    root.sourceText.insert('1', sourceDirectory)
     
def DestinationBrowse():
    # Opening the file-dialog directory prompting
    # the user to select destination folder to
    # which files are to be copied using the
    # filedialog.askopendirectory() method.
    # Setting initialdir argument is optional
    destinationdirectory = filedialog.askdirectory(initialdir = 'C:/')
 
    # Displaying the selected directory in the
    # root.destinationText Entry using
    # root.destinationText.insert()
    root.destinationText.insert('1', destinationdirectory)
     
def FileCheck():

    # Retrieving the destination location from the
    # textvariable using destinationLocation.get() and
    # storing in destination_location
    destination_location = destinationLocation.get()
    
    # Begin script to move files that have been edited in the last
    # 24 hours to FolderB. Assigning variables for current time, time
    # past, a string for displaying the time, then the home/created and destination
    # directories
    #
    # Using ".get" to get the source path and destination path from the Entry widgets.
    # Also assign variable that holds the name of the source path a different name,
    # since "source" is used later on.
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
    strftime = "%H:%M %m/%d/%Y"
    srcPath = root.sourceText.get()
    dest = root.destinationText.get()
    docs = os.listdir(srcPath)
    
    # Looping through the files present in the list
    for i in docs:
        # joining the source path with the file name, i.e. joining "srcPath" with "i", since
        # "srcPath" holds the path from the Entry widget, and "i" holds the name of the current file:
        source = os.path.join(srcPath, i)
        #get modified time of file
        st = os.path.getmtime(source)
        # my current time
        mtime = dt.datetime.fromtimestamp(st)
        # boolean to compare my current time to last 24 hours
        if mtime > ago:
            #moving files from argument
            shutil.move(source, dest)
                
    messagebox.showinfo("SUCCESSFULL", "Your file transfer was successful." )

    
# Creating object of tk class when utilized in scripts
# variables.
root = tk.Tk()
     
# Setting the title and background color
# as well as setting appropriate window frame size.
root.geometry("650x120")
root.title("Automatic File Transfer Interface")
root.config(background = "grey")
     
# Creating variables for tkinter to indentify StringVars in inputs.
sourceLocation = StringVar()
destinationLocation = StringVar()
     
# Calling the man Widgets() function to run our GUI.
Widgets()
     
# Defining infinite loop to keep window open.
root.mainloop()
