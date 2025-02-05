# TASK: Create a program that calculates the area of a rectangle.

# Ask the user for their name and greet them
name = input("What is your name? ").title().strip()
print(f"Hi {name}! Welcome to the area of a rectangle calculator program!")

while True:
    # Prompt the user to enter the length of the rectangle
    length = float(input(f"{name} please enter the length of your rectangle "))

    # Prompt the user to enter the width of the rectangle
    width = float(input(f"{name} please enter the width of your rectangle "))

    # Calculate the area using the formula: length * width
    area = (length * width)

    # Display the calculated area
    print(f"{name} the area of your rectangle is {area}" )

     # Ask the user if they want to do it again
    choice = input(f" {name} would you like to do another area of a rectangle calculation [y/n]? ").strip().lower()
    if choice == "y":
        pass
    else:
        break

 # Say goodbye
print(f"Thanks for using my program {name}!")
