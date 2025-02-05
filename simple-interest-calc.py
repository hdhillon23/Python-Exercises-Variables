# TASK: Create a program that calculates simple interest.

# Ask the user for their name and greet them
name = input("What is your name? ").title().strip()
print(f"Hi {name}! Welcome to the simple interest calculator program!")

while True:
    # Prompt the user to enter the principal amount
    print(f"{name} this is a simple interest calculator")
    principle_amount = float(input(f"{name} please enter the principle amount "))

    # Prompt the user to enter the annual interest rate (in percentage)
    anual_interest_rate = float(input(f"{name }please enter the annual interest rate (In percentage) "))
   
    # Prompt the user to enter the time period in years
    num_years = float(input(f"{name} please enter the time period in years"))

    # Calculate the simple interest using the formula
    intrest = (principle_amount * anual_interest_rate * num_years) / 10

    # Display the calculated simple interest
    print(f"{name} your interest will be {intrest} ")

    # Ask the user if they want to do it again
    choice = input(f" {name} would you like to do another simple interest calculation [y/n]? ").strip().lower()
    if choice == "y":
        pass
    else:
        break

 # Say goodbye
print(f"Thanks for using my program {name}!")