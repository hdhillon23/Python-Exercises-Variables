# TASK: Write a program that converts a temperature from Celsius to Fahrenheit.

# Ask the user for their name and greet them
name = input("What is your name? ").title().strip()
print(f"Hi {name}! Welcome to the temperature conversion program!")

while True:
    # Prompt the user to enter a temperature in Celsius
    print(f"Hello {name} this program converts temperatures from celsuis to fairenhiet")
    celsius = int(input("Whats your tempeture? Please answer in celsuis "))
   
    # Convert the Celsius temperature to Fahrenheit using the formula
    farhenhiet = (celsius * 9/5) + 32

    # Display the converted temperature
    print(f"{name} your given temperature in celsuis converts to {farhenhiet} farenhiet" )

    # Ask the user if they want to do it again
    choice = input(f" {name} would you like to do another temperature conversion [y/n]? ").strip().lower()
    if choice == "y":
        pass
    else:
        break

 # Say goodbye
print(f"Thanks for using my program {name}!")