## Day 10 - Exception Handling

Today, I learned how to **handle errors** in Python so the program doesn’t crash unexpectedly.  
Exception handling lets you catch problems and deal with them gracefully.

## Key Takeaways
- Use `try` and `except` to catch errors.
- You can handle **different types of exceptions** separately.
- The `finally` block runs no matter what — great for cleanup tasks.
- Always catch specific exceptions instead of using a bare `except`.

### Example
```python
try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except ValueError:
    print("That's not a valid number!")

try:
    result = 10 / int(input("Enter a divisor: "))
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero!")

try:
    f = open("sample.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("End of file operation.")
