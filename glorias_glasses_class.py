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
KIDS_GLASSES = 150.00
KIDS_SUNS = 75.00
DRY_EYE = 100.00
TEARS = 20.00

class GloriasGlasses:
    def __init__(self):
        self._qty_glasses = 0
        # Initialize parallel lists for menu items and prices
        self.glasses_items = ["Glasses", "Sun Glasses", "Kids Glasses", "Kids Sunglasses", "Dry Eye Kit", "Artificial Tears"]
        self.glasses_prices = [250.00, 175.00, 150.00, 75.00, 100.00, 20.00]
        # Initialize empty cart
        self.cart = []
    
    #@property
    #def name(self):
    #    return self._qty_glasses
    
    #@name.setter
    #def name(self, qty_glasses):
    #    self._qty_glasses = qty_glasses
    
    
    def get_glasses_items(self) -> list:
        return self.glasses_items
    
    def get_glasses_prices(self) -> list:
        return self.glasses_prices

    def display_menu(self) -> str:
        """Display Glorias Glasses Items and Prices"""
        display = ""
        for n in range(len(self.glasses_items)):
           display += f"{self.glasses_items[n]}     ${self.glasses_prices[n]}\n"
        return display


    def get_number_of_glasses(self) -> int:
        """Input validation on the customer must order at least one pair of glasses"""
        if self._number_glasses > 0:
            return self._number_glasses
        else:
            return 0

    def get_total_sale(self) -> float:
        """Return total sale from object
        
            Returns:
            _total_sale (float)"""
        return self._total_sale

    def calculate(self, number_glasses, number_suns, number_kid_glasses, number_kid_sun_glasses, number_dry_eye, number_art_tears: int = 1):
        """Calculate cost of the Glasses purchased
        
            Parameters:
            number_of_glasses (int)"""
        # TODO: Calculate cost of glasses purchased
        self.total_glasses = number_glasses * GLASSES_COST
        self._number_glasses = number_glasses
        self.total_suns = number_suns * SUNGLASSES_COST
        self.total_kid_glass = number_kid_glasses * KIDS_GLASSES
        self.total_kid_sun_glass = number_kid_sun_glasses * KIDS_SUNS
        self.total_dry_eye = number_dry_eye * DRY_EYE
        self.total_art_tears = number_art_tears * TEARS
        self._total_sale = self.total_glasses + self.total_suns + self.total_kid_glass + self.total_kid_sun_glass + self.total_dry_eye + self.total_art_tears

    