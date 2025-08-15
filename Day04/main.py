# Day 4: Logical operators and conditions

# Ask for age and check discount eligibility
age = int(input("How old are you? "))

if age < 8:
    print("You get a child discount! 🧒")
elif age >= 65:
    print("You get a senior discount! 👴")
else:
    print("Sorry, no discount this time!")

# Combine multiple conditions using and/or
height = int(input("What’s your height in cm? "))
has_pass = input("Do you have a ride pass? (yes/no): ").lower()

if height >= 120 and has_pass == "yes":
    print("You’re allowed to ride the roller coaster 🎢!")
else:
    print("Sorry, you can't ride.")

# Use not to flip a boolean
door_closed = input("Is the door closed? (yes/no): ").lower()

if not door_closed == "yes":
    print("Please close the door!")
else:
    print("Thanks for keeping it shut!")
