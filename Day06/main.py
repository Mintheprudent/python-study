# Day 6: Conditional Statements - Making Decisions

# Example 1: Basic if statement
weather = "rainy"

if weather == "rainy":
    print("Bring an umbrella!")
    
# Example 2: if-else
temperature = 10

if temperature >= 20:
    print("It's warm outside.")
else:
    print("It's chilly. Wear a jacket!")

# Example 3: if-elif-else
hour = 14

if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")

# Example 4: Nested if
is_raining = True
has_umbrella = False

if is_raining:
    if has_umbrella:
        print("You're safe from the rain.")
    else:
        print("You're going to get wet...")
