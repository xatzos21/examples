#VIRTUAL ENVIRONMENT EXERCISE
############################



# Using the skills  you have already + the knowledge available online,
# you are now to program a simple GUI (Graphical User Interface).


# A GUI is an interface that allows users to interacte with an electronical device or a program.
# Although being the job of mainly frontend developers, in backend also here is use of
# a GUI sometimes. As I showed you in 14 and 41 or even in the Lazy Script.
# The story program also had a form of GUI as you saw (graphical) what are the options, and
# could interact with the menu by giving input (as the user).


# FOR THIS YOU WILL NEED

# SOME SORT OF LIBRARY (so the venv makes sense)
# print() # to print a gui
# input() # to ask for user input
# if else # to use the user input for navigation through the menu
# CREATING A requirements.txt LISTING THE PROGRAM REQUIREMENTS


# FOR THIS YOU CAN USE

# loops   # to let a user stay in a specific menu until he wants to leave


# There is example code in this folder.


# REMEMBER: This is a VENV exercise. So creating a virtual environment before starting to code
# is essential. 

import time

def s_print(string):
    print(string)
    time.sleep(0.2)

loop = True

while loop == True:
    s_print("------")
    s_print("  --  ")
    s_print("------")
    s_print("Make a choice: (1) Menu 1  (2) Menu 2")
    choice = input("Menu: ")
    if choice == ("1"):
        s_print("Welcome to Menu 1")
        s_print("Please choose folder: (1) A  (2) B")
        x = input("Folder:")
        if x == ("1"):
            s_print("Folder A!")
        elif x == ("2"):
            s_print("Folder B!")
    elif choice ==("2"):
        s_print("Welcome to Menu 2")
        s_print("Please choose folder: (1) C  (2) D")
        y = input("Folder: ")
        if y == ("1"):
            s_print("Folder C!")
        elif y == ("2"):
            s_print("Folder D!")
    else:
        s_print("Wrong Input")
    loop =False