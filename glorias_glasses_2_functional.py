"""
 Name: glorias_glasses_2.py
 Author: Jesse Bunnell
 Created: 09/02/2023
 Purpose:  Functional POS program
"""

import utils

# TODO: Cost of glasses for customer
GLASSES_COST = 250.00
SUNGLASSES_COST = 175.00

def main():
    glasses_total = get_input()
    total_sale = calculate(glasses_total)
    display(total_sale)

def get_input():
    # TODO: Get input from user how may glasses sold
    glasses = utils.get_int("Enter the number of glasses sold: ")
    #suns = utils.get_int("Enter the number of sunglasses sold: ")
    return glasses#, suns

def calculate(glasses):
    # TODO: Calculate cost of glasses purchased
    total_glasses = glasses * GLASSES_COST
    #total_suns = suns * SUNGLASSES_COST
    total_sale = total_glasses# + total_suns
    return total_sale

def display(total_sale):
    # TODO: Display transaction for customer
    print(f"Your total for your glasses is: ${total_sale:,.2f}")


if __name__ == "__main__":
    main()