"""
 Name: glorias_glasses_class.py
 Author: Jesse Bunnell
 Created: 09/10/2023
 Purpose:  Class POS program
"""

import utils

# TODO: Cost of glasses for customer
GLASSES_COST = 250.00
SUNGLASSES_COST = 175.00

class GloriasGlasses:
    def __init__(self):
        pass

    def get_number_of_glasses(self):
        # Validation
        if self._number_glasses > 0:
            return self._number_glasses
        else:
            return 0

    def get_total_sale(self):
        return self._total_sale

    def calculate(self, number_glasses):
        # TODO: Calculate cost of glasses purchased
        self._total_sale = number_glasses * GLASSES_COST
        self._number_glasses = number_glasses
        #self.total_suns = suns * SUNGLASSES_COST
        #self.total_sale = self.total_glasses + self.total_suns

    