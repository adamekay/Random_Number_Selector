import random
import sys

tries = []
tries_int = 0

try:
    selection = int(input("What number would you like to have randomly selected? "))
except:
    for i in range(3):
        try:
            selection = input("Please give a whole number value.\nWhat number would you like to have randomly "
                              "selected? ")
        except:
            if i == 2:
                print("Closing Program.")
                exit()
            continue
        break

try:
    range = int(input("\nWhat do you want the range of your selection to be? (i.e., 10, 50, etc.) "))
except:
    for i in range(3):
        try:
            selection = int(input("Please give a whole number value.\nWhat do you want the range of your selection to "
                                  "be? "))
        except:
            if i == 2:
                print("Closing Program.")
                exit()
            continue
        break


def appearances(number):
    global appearances_specific
    appearances_specific = 0
    for j in tries:
        if number == j:
            appearances_specific += 1


while True:
    integer = random.randint(0, range)
    tries.append(integer)
    tries_int += 1
    if integer == selection:
        print("It took {} tries to get the number {} from a random roll of {} numbers".format(tries_int, selection, range))
        tries.sort()
        print(tries)
        break

# Now I'm going to display how many times each value occurred. i.e; if "4" loaded up 10 times, it will say so.

# A unique_rolls set was created to avoid duplicates. And then new list was created with non-repeats.

unique_rolls = set()
for i in tries:
    unique_rolls.add(i)

tries2 = []
for i in unique_rolls:
    tries2.append(i)
tries2.sort()

for i in tries2:
    appearances(i)
    if appearances_specific != 0:
        print("The number {} appeared {} times in this roll.".format(i, appearances_specific))

