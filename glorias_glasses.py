"""
 Name: glorias_glasses.py
 Author: Jesse Bunnell
 Created: 09/02/2023
 Purpose:  POS program
"""

import utils

# TODO: Cost of glasses for customer
GLASSES_COST = 250.00
SUNGLASSES_COST = 175.00

# TODO: Get input from user how may glasses sold
glasses = utils.get_int("Enter the number of glasses sold: ")
suns = utils.get_int("Enter the number of sunglasses sold: ")

# TODO: Calculate cost of glasses purchased
total_glasses = glasses * GLASSES_COST
total_suns = suns * SUNGLASSES_COST
total_bill = total_glasses + total_suns

# TODO: Diplay transaction for customer
print(f"Your total for your glasses is: ${total_bill:,.2f}")

