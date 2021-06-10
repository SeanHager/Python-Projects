#
# Python:   3.9.5
# SQLite:   3.12.2
#
# Author:   Sean Hager
#
# Purpose:  The Tech Academy - Python Course, Creating a script assignment.
#           Demonstrating how to write a script that creates a database and adds new data into that database.
#       
#           Primary task is creating a function with tuple and looping through tuple to only add files with
#           '.txt' extension. Script then prints out added values in Python shell to user.
#




import sqlite3


conn = sqlite3.connect('python_sqlite.db') 

# Create a database with tbl_doctype and a column named col_extension
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_doctype(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_extension TEXT)") 
    # Commiting all table changes    
    conn.commit()
    
conn = sqlite3.connect('python_sqlite.db')


# Tuple of file names for database
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# For loop to loop through tuple and only add into our table the files ending with '.txt'
for x in fileList:
    # create if statement with x.endswith to choose values from tuple that match our query in our loop.
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # (x, )) is our one-tuple
            cur.execute("INSERT INTO tbl_doctype(col_extension) VALUES (?)", (x, )) 
        print(x)
conn.close()
