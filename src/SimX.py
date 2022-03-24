# SimX
#
#
# Purpose: Little Simulation Game in Python
#
# License: GNU GPL v2
#
#
# Author: micziz and all contributors.


# Import Standard Modules
import os, time, random, sys

# Import non standard modules
import pyfiglet

# Version number.
version = "0.1.0"
# Copyright.
copyrigth = "Copyrigth© micziz 2022-present"
# Credits
credits = {
    "micziz",
}
# Clear commands
clear = "clear"

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
    #Welcome the player
    print("Welcome to SimX!")
    # Try to load the save
    print("Locating save...")
    # Decleare the golbal var
    global name
    def loadsave():
        # Using try except
        try:
            # Try to open the file in read mode
            f = open("src/name.txt", "rt")
        #If it runs into an exception:
        except FileNotFoundError:
            #Create the save
            print("Save not found")
            #Ask for name
            name = input("Whats your name?: ")
            #Save the name
            f = open("src/name.txt", "wt")
            f.write(name)
            #Will send you to tutorial
            print("Sending you to the tutorial")
            tutorial()
        #Read the lines
        save = f.readlines()
        #Print the name
        for name in save:
            print(f"Welcome {name}!")
        #And it sends you to the home.
        print(f"Sending you to home")
    #Run the function to loadsave
    loadsave()
    #Go home.
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
    #Print that these are section commands
    print("Attension theshe are section commands. There are help sections in those sections.")
    #Actual commands
    commands = {
        "Help: Opens the help section.",
        "Home: Brings you home",
        "Work: Opens the work section",
        "Bank: Opens the bank section",
        "Buy: Opens the buy section",
        "Sell: Opens the sell section",
    }
    #Print the commands
    for command in commands:
        print(command)
    #Print that these are global commands
    print("Here are some global commands:")
    #Actual Commands
    globalcommands = {
        "Clear: Clear all the console",
        "Copyright: Tells you copyright",
        "Credits: Credits of the game", 
    }
    #Print them
    for globalcommand in globalcommands:
        print(globalcommand)
    

#Help section
def help():
    #Welcome to the help section
    print("Welcome to the help section!")
    #Purpose of the help section
    print(
        "Here you can re do the tutorial using the tutorial command, or get a list of commands using commands"
    )
    while True:
        selecthelp = input()
        if selecthelp == "tutorial":
            tutorial()
        elif selecthelp == "commands":
            commands()
        elif selecthelp == "home":
            home()
        else: 
            print("Not a command")


def work():
    place = "work"
    fired = False
    while True:
        print(f"currently at {place}")
        print("Welcome. Heres your options:")
        def getnewwork():
            filef = "src/works.txt"
            word = open(filef, "rt").read().splitlines()
            job = random.choice(word)
            print(f"Your new job is: {job}")
            fired = False
        print("1 = Work")
        print("2-Fire yourself")
        selectwork = input()
        if selectwork == "1":
            if fired == True:
                getnewwork()
            else:
                print("Working...")
                rng = random.randint(1, 5)
                time.sleep(rng)
                salary = 100
                salarys = str(salary)
                print(f"You got your salary, witch is {salarys}$ dollars.")
                global value
                value = value + salary
        elif selectwork == "2":
            print("You fired yourself from your job")
        elif selectwork == "home":
            home()


def bank():
    place = "bank"
    while True:
        print(f"currently at {place}")
        print("Welcome to bank.")
        print("Here are your options:")
        print("1 = value")
        print("2 = Donate 5 dollars to charity")
        print("3 = Wipe")
        selectbank = input()
        if selectbank == "1":
            global value
            print("Value in $:")
            print(value)
            time.sleep(3)
        elif selectbank == "2":
            print("Thanks")
            value = value - 5
            print(value)
        elif selectbank == "3":
            value = value % 2
            print("Half of your bank was snapped out of existance")
        elif selectbank == "home":
            home()


def buy():
    global item1time, item2time
    items = ["Strawberry", "Cheese", "Vinager", "Chips", "Milk", "Ham", "Turkey"]
    item1 = random.choice(items)
    item2 = random.choice(items)
    item1time = random.randint(1, 5)
    item2time = random.randint(1, 5)
    print(f"You bougth {item1} x" + str(item1time) + f" and {item2} x" + str(item2time))

    def getoutmoney():
        global subitem1time, subitem2time, value
        subitem1time = item1time * 10
        value = value - subitem1time
        subitem2time = item2time * 10
        value = value - subitem2time

    getoutmoney()
    time.sleep(2)
    home()


def sell():
    global value, subitem1time, subitem2time
    value = subitem1time + value
    value = subitem2time + value
    print("Sold everything...")
    time.sleep(2)


def home():
    os.system(clear)
    place = "home"
    tipr = open("src/tips.txt", "rt")
    tips = tipr.readlines()

    while True:
        tip = random.choice(tips)
        print(tip)
        selecthome = input(f"Currently at {place}: ")
        if selecthome == "work":
            work()
        elif selecthome == "help":
            help()
        elif selecthome == "bank":
            bank()
        elif selecthome == "buy":
            buy()
        elif selecthome == "sell":
            sell()
        elif selecthome == "version":
            print(version)
        elif selecthome == "credits":
            for credit in credits:
                print(credit)
        elif selecthome == "copyrigth":
            print(copyrigth)
        elif selecthome == "clear":
            os.system(clear)


start()
