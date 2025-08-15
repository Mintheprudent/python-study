## Day 9 - Modules and Imports

Today, I learned how to **use modules** in Python to keep code organized and reusable.  
Modules are Python files with code that you can import and use in other files.

## Key Takeaways
- **Built-in modules** come with Python (e.g., `math`, `datetime`, `random`).
- Use `import module_name` to bring in a module.
- Use `import module_name as alias` to shorten names.
- Use `from module_name import function` to import specific functions.

### Example
```python
import math
print(f"Square root of 16 is {math.sqrt(16)}")
print(f"Pi value is {math.pi}")

import datetime as dt
print(f"Today's date is {dt.date.today()}")

from random import randint, choice
print(f"Random number between 1 and 10: {randint(1, 10)}")
print(f"Random choice from list: {choice(['apple', 'banana', 'cherry'])}")
