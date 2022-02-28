# Import os to use system commands time to sleep and random to randomize
import os, time, random
from pyfiglet import Figlet

version = "0.2.1"
copyrigth = "Copyrigth© micziz 2022-present"
credits = {
    "micziz",
}
clear = "clear"
os.system(clear)
fi = Figlet(font="big")
print(fi.renderText("SimX"))

# Clear command to clear the shell
clear = "clear"
# Starting value, can be changed
value = 100
# Tutorial functions
def tutorial():
    # Clear the console
    os.system(clear)
    # Intro
    print("Welcome to a short Interactive tutorial for SimX!")
    # Sleep
    time.sleep(3)
    print("This tutorial assumes no prior experience")
    time.sleep(3)
    print("Let's go!")
    time.sleep(3)
    os.system(clear)
    # Actual tutorial
    print(
        "By deafault you are at home. If you ever find yourself lost, use the home command to go home"
    )
    time.sleep(3)
    os.system(clear)
    print(
        "To get yourself some things you gotta work kid! Use work to open the work menu"
    )
    time.sleep(3)
    os.system(clear)
    print("Use the bank command to open the bank menu!")
    time.sleep(3)
    os.system(clear)
    print(
        "If you ever find yourself stuck, use the help command to re do this interactive tutorial, or to get a list of all commands."
    )
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
    print(
        "Here you can re do the tutorial using the tutorial command, or get a list of commands using commands"
    )
    selecthelp = input()
    if selecthelp == "tutorial":
        tutorial()
    else:
        commands()


def work():
    place = "work"
    fired = False
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
            print("You got your salary, witch is 100$ dollars.")
            global value
            salary = 100
            value = value + salary
    elif selectwork == "2":
        print("You fired yourself from your job")
    time.sleep(3)
    home()


def bank():
    place = "bank"
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
    time.sleep(2)
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
    tip = random.choice(tips)
    print(tip)

    while True:
        selecthome = input(f"\nCurrently at {place}: ")
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


start()
