## Day 12 - Built-in Functions & External Modules

Today, I learned how to use Python's **built-in functions** and **external modules** (standard library).  
Built-in functions are always available without importing anything,  
while external modules need to be imported before use.

---

## Key Takeaways
- **Built-in functions**: No need to import, e.g., `len()`, `max()`, `min()`, `sum()`, `sorted()`.
- **External modules**: Part of Python's standard library, but require `import`.
  - `math` → mathematical functions and constants.
  - `random` → random number generation.
  - `datetime` → date and time handling.

---

### Example
```python
# Built-in functions
numbers = [3, 7, 1, 9, 2]
print(len(numbers))      # 5
print(max(numbers))      # 9
print(min(numbers))      # 1
print(sum(numbers))      # 22
print(sorted(numbers))   # [1, 2, 3, 7, 9]

# External modules
import math
print(math.sqrt(16))     # 4.0

import random
print(random.randint(1, 10))

import datetime
print(datetime.date.today())
