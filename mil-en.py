"""
This is a mock program to query potential candidates about their interest in joining the military.
Asks for age to determine eligibility to serve in the military.
@author: Jamin Kiplagat and Tony Kipkemboi
@date: January 16th, 2021
"""
import sys
import time


def enlist_or_nah():
    # loop based on input
    agree = input("Do you want to join the military: Y/N ")

    # loop according to input given by user
    # if Y, open conversation
    if agree == "Y" or agree == "y":
        print()
        time.sleep(1)
        print("Great decision! \nNow we will ask you some questions...")

    # if N, return when you want to join
    elif agree == "N" or agree == "n":
        print()
        time.sleep(1)
        print("Come back when you are ready.")
        # system exits if N
        sys.exit()

    # if input is not Y/N, warn invalid input
    else:
        print()
        time.sleep(1)
        print("Invalid input! \nTry again.")
        print()
        time.sleep(1)
        # loop again to the beginning until a correct entry is made
        enlist_or_nah()


def age_limit():
    # ask for age
    age = float(input("How old are you: "))

    # eligibility age
    eligibility_age = "17 to 35"

    # raise Value Error if age is <=0
    if age <= 0:
        raise ValueError("Age cannot be <= 0!")

    # if age is >= 35, too old to join
    elif age >= 35:
        print()
        time.sleep(1)
        print("You are too old to join the military")
        print("(Eligibility age to join is between " + eligibility_age + " years old.)")

    # if age <= 16, too young to join and give time remaining
    elif age <= 16:
        remainder = (17 - age)
        print()
        time.sleep(1)
        print("You are too young, try again in the next " + str(remainder) + " year(s).")
        print("(Eligibility age to join is between " + eligibility_age + " years old.)")

    # if age is between 17 - 35, eligible to join
    elif 17 <= age <= 35:
        print()
        time.sleep(1)
        print("You are eligible to join the military!")

    else:
        print()
        time.sleep(1)
        print("invalid age! \nTry again.")
        # loop again to the beginning until a correct entry is made
        time.sleep(1)
        age_limit()


# main method/function to run the other methods
# prints welcome message
def main():
    print("******************")
    print("\t\t\t\t THE KENYA ARMY! \t\t\t")
    print("******************")
    print("\t Come join the Greatest Team on Earth! \t\t")
    print("\t\t\t Recruitment Fair! \t\t\t")
    print("******************")
    enlist_or_nah()
    print()
    age_limit()


# this prints everything in main method (to include the entire program)
if _name_ == "_main_":
    main()
