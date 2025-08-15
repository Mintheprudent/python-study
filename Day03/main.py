# Day 3: Using elif and nested conditionals

# Ask for temperature
temp = int(input("What's the temperature today? "))

if temp >= 30:
    print("It’s super hot. Don’t forget to drink water!")
elif temp >= 20:
    print("Perfect weather. Maybe go for a walk?")
elif temp >= 10:
    print("Bit chilly. Wear something warm.")
else:
    print("Freezing! Bundle up like a penguin!")

# Ask user what they're carrying
weather = input("Is it raining? (yes/no) ").lower()

if weather == "yes":
    umbrella = input("Did you bring an umbrella? (yes/no) ").lower()
    if umbrella == "yes":
        print("Great! You’re all set.")
    else:
        print("You might want to find some shelter.")
else:
    print("No rain? Lucky day!")
