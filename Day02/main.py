# Day 2: Getting user input and using conditional statements

# Ask for user's name
name = input("What’s your name? ")
print("Hi there, " + name + "!")

# Ask for age and convert to integer
age = int(input("How old are you? "))
if age >= 20:
    print("You're an adult!")
else:
    print("You're still a minor!")

# Ask for a number and check if it's even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("That's an even number.")
else:
    print("That's an odd number.")
