# # import datetime module
# import datetime as dt

# # Creating a datetime object
# x = dt.datetime(2020, 5, 17)
# print(x)

# import math

# # Accessing the value of pi
# x = math.pi
# print(x)

# # Printing numbers from 100 to 109
# for i in range(100, 110):
#     print(i)

# # Printing the days of the week
# for days in range(0, 7):
#     print("day", days + 1)

# # Generating a random number
# import random

# mynumber = random.randint(1, 100)
# print(mynumber)

# # Random number guessing game
# import random

# for number in range(10):
#     x = random.randint(1, 1000000)
#     input("Enter the value of your guess number ")
#     if x <= 500000:
#         print("too low")
#     else:
#         print("too high")

# Defining a function to roll a dice
import random

def rollDice():
    dice = random.randint(1, 6)
    print("You rolled:", dice)

for i in range(6):
    rollDice()

def whichcake(ingredient):
    if ingredient == "chocolate":
        print("Chocolate meals are amazing")
    elif ingredient == "broccoli":
        print("Broccoli is another great ingredient")
    else:
        print("Yours is great too, I suppose")

# Testing the whichcake function
whichcake("broccoli")

