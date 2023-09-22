"""
 Name: glorias_glasses_3.py
 Author: Jesse Bunnell
 Created: 09/02/2023
 Purpose:  OOP POS program
"""

import utils

# TODO: Cost of glasses for customer
GLASSES_COST = 250.00
SUNGLASSES_COST = 175.00


class GloriasGlasses:
    def __init__(self):
        pass

    def get_input(self):
        # TODO: Get input from user how may glasses sold
        self.glasses = utils.get_int("Enter the number of glasses sold: ")
        self.suns = utils.get_int("Enter the number of sunglasses sold: ")

    def calculate(self):
        # TODO: Calculate cost of glasses purchased
        self.total_glasses = self.glasses * GLASSES_COST
        self.total_suns = self.suns * SUNGLASSES_COST
        self.total_sale = self.total_glasses + self.total_suns

    def display(self,):
        # TODO: Display transaction for customer
        print(f"Your total for your glasses is: ${self.total_sale:,.2f}")


glorias_glasses = GloriasGlasses()
glorias_glasses.get_input()
glorias_glasses.calculate()
glorias_glasses.display()