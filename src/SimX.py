# SimX
#
#
# Purpose: Little Simulation Game in Python
#
# License: GNU GPL v2
#
#
# Author: micziz


# Import Standard Modules
import os, time, random, sys

# Import non standard modules
import pyfiglet

# Version number.
version = "0.1.0"
# Copyright.
copyright = "Copyright© micziz 2022-present"
# Credits
credits = {
    "micziz (miczicontent@gmail.com)",
}
author = "micziz (miczicontent@gmail.com)"
# Clear commands
clear = "clear"
# License command
license = "SimX is licensed under the GNU GPL 2.0"
# Info command
info = f"""
SimX V {version}. 
This program is free softwere. Source code is available at https://www.github.com/micziz/SimXV2
Liscenced under the GNU GPL 2.0
Copyright© micziz 2022-present
"""

################################################################START################################################################
# Clear the console
os.system(clear)
# Stamp a figlet title.
fi = pyfiglet.Figlet(font="big")
print(fi.renderText("SimX"))
# Starting value, can be changed
value = 100
# Start function
def start():
    # Welcome the player
    print("Welcome to SimX!")
    # Try to load the save
    print("Locating save...")
    # Declare the global variable's
    global name

    def loadsave():
        # Using try except
        try:
            # Try to open the file in read mode
            f = open("src/name.txt", "rt")
        # If it runs into an exception:
        except FileNotFoundError:
            # Create the save
            print("Save not found")
            # Ask for name
            name = input("Whats your name?: ")
            # Save the name
            f = open("src/name.txt", "wt")
            f.write(name)
            # Will send you to tutorial
            print("Sending you to the tutorial")
            tutorial()
        # Read the lines
        save = f.readlines()
        # Print the name
        for name in save:
            print(f"Welcome {name}!")
        # And it sends you to the home.
        print(f"Sending you to home")

    # Run the function to loadsave
    loadsave()
    time.sleep(2)
    # Go home.
    home()


def tutorial():
    # Clear the console
    os.system(clear)
    # Intro
    print("Welcome to a short tutorial for SimX!")
    # Sleep
    time.sleep(2)
    # Actual tutorial
    # Home
    print(
        "Home is your center of operation. If you ever find yourself lost, use the home command to go home"
    )
    time.sleep(2)
    # Work
    print(
        "To get yourself some things you gotta work kid! Use work to open the work menu"
    )
    time.sleep(2)
    # Bank
    print("Use the bank command to open the bank menu!")
    time.sleep(2)
    # help
    print(
        "If you ever find yourself stuck, use the help command to redo this tutorial, or to get a list of all commands."
    )
    time.sleep(2)
    print("This is everything! Sending you home!")
    home()


# Commands section
def commands():
    # Print that these are section commands
    print(
        "Attension theshe are section commands. There are help sections in those sections."
    )
    # Actual commands
    commands = {
        "Help: Opens the help section.",
        "Home: Brings you home",
        "Work: Opens the work section",
        "Bank: Opens the bank section",
        "Buy: Opens the buy section",
        "Sell: Opens the sell section",
    }
    # Print the commands
    for command in commands:
        print(command)
    # Print that these are global commands
    print("Here are some global commands:")
    # Actual Commands
    globalcommands = {
        "Clear: Clear all the console",
        "Copyright: Tells you copyright",
        "Credits: Credits of the game",
    }
    # Print them
    for globalcommand in globalcommands:
        print(globalcommand)


# Help section
def help():
    # Welcome to the help section
    print("Welcome to the help section!")
    # Purpose of the help section
    print(
        "Here you can re do the tutorial using the tutorial command, or get a list of commands using commands"
    )
    # While True loop for the help section
    while True:
        # input
        selecthelp = input("Use help to get help!")
        # Check for input
        if selecthelp == "tutorial":
            # Tutorial function call
            tutorial()
        elif selecthelp == "commands":
            # Commands call
            commands()
        elif selecthelp == "home":
            # Home function call
            home()
        else:
            # Fallout command
            print("Not a command")


# Work function
def work():
    # Declare that the place is work
    place = "work"
    # Declare that you are not fired
    fired = False
    # Print where you are
    print(f"currently at {place}")
    # Welcome to the place
    print("Welcome. Heres your options:")
    # Function to get a new job
    def getNewJob():
        # Open the file for jobs
        filef = "src/files/jobs.txt"
        # Read it
        jobs = open(filef, "rt").read().splitlines()
        # Random.choice to select it
        job = random.choice(jobs)
        # Announce the new job
        print(f"Your new job is: {job}")
        # No longer fired
        fired = False

    #Options
    print("1 = Work")
    print("2-Fire yourself")
    #while True
    while True:
        #get input
        selectwork = input("Need Help? Type help.")
        #if it's equal to 1
        if selectwork == "1":
            #and you are fired
            if fired == True:
                #Get a new job
                getNewJob()
            #else
            else:
                #print that you are forking
                print("Working...")
                #time to work
                rng = random.randint(1, 5)
                time.sleep(rng)
                #TODO May add diffrent salary
                #salary
                salary = 100
                #Transfor for str
                salarys = str(salary)
                #Print that it ended
                print(f"You got your salary, witch is {salary}$ dollars.")
                global value
                #add Value
                value = value + salary
        #if it's equal to 2
        elif selectwork == "2":
            #You are fired
            print("You fired yourself from your job")
        #if it's equal to help
        elif selectwork == "help":
            #Reprint help
            print("1 = Work")
            print("2-Fire yourself")
        #go home command
        elif selectwork == "home":
            #home
            home()
        else:
            print("Not a command!")


def bank():
    place = "bank"
    print(f"currently at {place}")
    print("Welcome to bank.")
    print("Here are your options:")
    print("1 = value")
    print("2 = Donate 5 dollars to charity")
    print("3 = Wipe")
    while True:
        selectbank = input("Type help if you feel stuck")
        if selectbank == "1":
            global value
            print("Value in $:")
            print(value)
            time.sleep(3)
        elif selectbank == "2":
            print("Thanks For donating!")
            value = value - 5
            print(value)
        elif selectbank == "3":
            value = value % 2
            print("Half of your bank was snapped out of existence")
        elif selectbank == "home":
            home()
        elif selectbank == "help":
            print("1 = value")
            print("2 = Donate 5 dollars to charity")
            print("3 = Wipe")
        else:
            print("Not a command!!!")


def addInventory(i1, it1):
    inventory = []
    inventorytime = []
    inventory.append(i1)
    inventorytime.append(it1)


# Sell function
def sell():
    # global variables
    global value, subitem1time
    # Sell everything
    value = subitem1time + value
    # Print it out
    print("Sold everything...")
    time.sleep(2)


# Buy function
def buy():
    # Decleare some global variables
    global item1time
    # Open the things to buy file
    fttb = open("src/files/ttb.txt", "rt")
    # Gee items
    item = fttb.readlines()
    # Decleare a List
    items = []
    # append
    items.append(item)
    # Get and decleare items.
    item1 = random.choice(items)
    item1time = random.randint(1, 5)
    # sleep
    time.sleep(2)
    # Remove moeny from the bank account
    def getoutmoney():
        global subitem1time, value
        subitem1time = item1time * 10
        value = value - subitem1time

    getoutmoney()
    addInventory(item1, item1time)
    os.system(clear)
    item1 = random.choice(item1)
    print(f"You bought {item1} x" + str(item1time))
    time.sleep(2)
    home()


# Home function
def home():
    #Clear the console
    os.system(clear)
    #Decleare that the place is Home
    place = "home"
    #Open tips.txt
    tipr = open("src/files/tips.txt", "rt")
    #Read the tips
    tips = tipr.readlines()
    #while True...
    while True:
        #Select a random tip
        tip = random.choice(tips)
        #Print it
        print(tip)
        # Print the current place
        selecthome = input(f"Currently at {place}: ")
        #Check for comamnds:
        if selecthome == "work":
            #work
            work()
        elif selecthome == "help":
            #help
            help()
        elif selecthome == "bank":
            #bank
            bank()
        elif selecthome == "buy":
            #buy
            buy()
        elif selecthome == "sell":
            #Sell
            sell()
        elif selecthome == "version":
            #version
            print(
                f"Current SimXV2 version: {version}. SimX Follows semantic versioning!"
            )
        elif selecthome == "credits":
            #credits
            print("OG Author:")
            print(author)
            print("Contributors:")
            for credit in credits:
                print(credit)
        elif selecthome == "copyright":
            #copyright
            print(copyright)
        elif selecthome == "clear":
            #clear
            os.system(clear)
        elif selecthome == "author":
            #author
            print(author)
        elif selecthome == "license":
            #license
            print(license)
        elif selecthome == "info":
            #info
            print(info)
        else:
            #else
            print("Not a command!")

#----------------------------------------------------------------Start function----------------------------------------------------------------



start()
