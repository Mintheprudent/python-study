# Day 10 - Exception Handling
# Today we learned how to handle errors in Python using try-except blocks.

# Basic try-except
try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except ValueError:
    print("That's not a valid number!")

# Handling multiple exceptions
try:
    result = 10 / int(input("Enter a divisor: "))
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero!")

# Using finally
try:
    f = open("sample.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("End of file operation.")
