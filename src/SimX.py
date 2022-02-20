import os, time, random
clear = 'clear'
value = 100
def tutorial():
    os.system(clear)
    print("Welcome to a short Interactive tutorial for SimX!")
    time.sleep(3)
    print("This tutorial assumes no prior experience")
    time.sleep(3)
    print("Let's go!")
    time.sleep(3)
    os.system(clear)
    print("By deafault you are at home. If you ever find yourself lost, use the home command to go home")
    time.sleep(3)
    os.system(clear)
    print("To get yourself some things you gotta work kid! Use work to open the work menu")
    time.sleep(3)
    os.system(clear)
    print("Use the bank command to open the bank menu!")
    time.sleep(3)
    os.system(clear)
    print("If you ever find yourself stuck, use the help command to re do this interactive tutorial, or to get a list of all commands.")
    time.sleep(3)
    print("This is everything! Sending you home!")

    home()
def commands():
    commands = {
        "Help: Opens the help section.",
        "Tutorial: Opens the tutorial section",
        "Commands: Opens this section, the commands section",
        "Copyright: Tells you copyright",
        "Credits: Credits of the game",
        "Home: Brings you home", 
    }
    for command in commands:
        print(command)

def start():
    print("Welcome to SimX!")
    name = input("What's your name? ")
    print(f"Welcome {name}!")
    time.sleep(2)
    print("Ever played?")
    checkifplayed = input()
    if checkifplayed == "y":
        print("Ok, creating a new game")
    else:
        tutorial()
    print("Teleporting you to home!")
    home()

def help():
    print("Welcome to the help section!")
    print("Here you can re do the tutorial using the tutorial command, or get a list of commands using commands")
    selecthelp = input()
    if selecthelp == "tutorial":
        tutorial()
    else:
        commands()


def work():
    place = "work"
    print(f"currently at {place}")
    print("Welcome. Heres your options:")
    print("1 = Work")
    selectwork = input()
    if selectwork == "1":
        print("Working...")
        rng = random.randint(1, 5)
        time.sleep(rng)
        print("You got your salary, witch is 100$ dollars.")
        global value
        salary = 100
        value = value + salary
    home()

def bank():
    print("Welcome to bank.")
    print("Here are your options:")
    print("1 = value")
    selectbank = input()
    if selectbank == "1":
        global value
        print("Value in $:")
        print(value)
    home()

def home():
    os.system(clear)
    place = "home"
    tips = ["Remember, help can be obtaiend with the help command"]
    while True:
        selecthome = input(f"\nCurrenly at {place}.")
        if selecthome == "work":
            work()
        elif selecthome == "help":
            help()
        elif selecthome == "bank":
            bank()
start()



