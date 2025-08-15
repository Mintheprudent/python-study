# Day 12 - Built-in Functions & External Modules
# Today we learned about Python's built-in functions and how to use external modules.

# --- Built-in Functions ---
numbers = [3, 7, 1, 9, 2]

print("Length:", len(numbers))           # len() - length of the list
print("Max value:", max(numbers))        # max() - maximum value
print("Min value:", min(numbers))        # min() - minimum value
print("Sum:", sum(numbers))              # sum() - sum of elements
print("Sorted:", sorted(numbers))        # sorted() - returns a sorted list

# --- External Modules (built-in library imports) ---
import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

import random
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(numbers))

import datetime
print("Today's date:", datetime.date.today())
