"""
 Name: glorias_glasses_main_cli.py
 Author: Jesse Bunnell
 Created: 09/10/2023
 Purpose:  Main POS program
"""

import utils
import glorias_glasses_class as glasses


def get_input():
    # TODO: Get input from user how may glasses sold
    glasses = utils.get_int("Enter the number of glasses sold: ")
    # suns = utils.get_int("Enter the number of sunglasses sold: ")
    return glasses  # and suns


def display():
    # TODO: Display transaction for customer
    number_glasses = glorias_glasses.get_number_of_glasses()
    total_sale = glorias_glasses.get_total_sale()
    print(f"Total number of glasses {number_glasses}")
    print(f"Your total for your glasses is: ${total_sale:,.2f}")


number_glasses = get_input()
glorias_glasses = glasses.GloriasGlasses()
glorias_glasses.calculate(number_glasses)
display()
