"""
Name:    utils.py
Author:  Jesse Bunnell
Created: 02/22/2023
Purpose: Contains general utility functions
"""

def get_int(prompt):

    # Declare local variable
    num = 0
    num = input(prompt)

    try:
        return int (num)

    except ValueError:
        print(f"You enter: {num}, which is not a whole number.")
        print(f"Let's try that again.\n")

        return get_int(prompt)

def get_float(prompt):
    
    num = 0

    num = input(prompt)

    try:
        return float(num)
    
    except ValueError:
        print(f"You enter: {num}, which is not a number.")
        print(f"Let's try that again.\n")

        return get_float(prompt)


def main():
    print(title("Print Title Test!"))

def title (statement):
    # Get the length of the statement string variable
    text_length = len(statement)

    # Create the title string
    result = ""
    result = result + "+--" + "-" * text_length + "--+\n"
    result = result + "|  " + statement + "  |\n"
    result = result + "+--" + "-" * text_length + "--+\n"

    return result

if __name__ == "__main__":
    main()