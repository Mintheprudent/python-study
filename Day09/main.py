# Day 9 - Modules and Imports
# Today we learned how to organize code using modules and how to import them.

# Importing a built-in module
import math

# Using a function from the math module
print(f"Square root of 16 is {math.sqrt(16)}")
print(f"Pi value is {math.pi}")

# Importing with an alias
import datetime as dt
print(f"Today's date is {dt.date.today()}")

# Importing specific functions
from random import randint, choice

print(f"Random number between 1 and 10: {randint(1, 10)}")
print(f"Random choice from list: {choice(['apple', 'banana', 'cherry'])}")
