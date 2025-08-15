# Day 7 - Loops and Iterations

Today, I practiced using **for loops** and **while loops** in Python.  
These loops are powerful for repeating actions without writing the same code multiple times.

## Key Takeaways
- **For loops** are great when you know how many times to loop or when looping through a collection.
- **While loops** run until a certain condition becomes `False`.
- The `range()` function is super useful for generating sequences of numbers.

### Example
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
