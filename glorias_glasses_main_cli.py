"""
 Name: glorias_glasses_main_cli.py
 Author: Jesse Bunnell
 Created: 09/10/2023
 Purpose:  Main POS program
"""

import utils
import glorias_glasses_class 
glasses = glorias_glasses_class.GloriasGlasses()

def get_glasses():
    # TODO: Get input from user how many glasses sold
    glasses = utils.get_int("Enter the number of glasses sold: ")
    # suns = utils.get_int("Enter the number of sunglasses sold: ")
    return glasses  # and suns

def get_suns():
    # TODO: Get input from user how many sun glasses sold
    suns = utils.get_int("Enter the number of sunglasses sold: ")
    return suns

def get_kid_glasses():
    # TODO: Get input from user how many kids glasses sold
    kid_glasses = utils.get_int("Enter the number of kids glasses sold: ")
    return kid_glasses

def get_kid_sun_glasses():
    # TODO: Get input from user how many kids sun glasses sold
    kid_sun_glasses = utils.get_int("Enter the number of kids sun glasses sold: ")
    return kid_sun_glasses

def get_dry_eye():
    # TODO: Get input from user how many dry eye kits were sold
    dry_eye = utils.get_int("Enter the number of Dry Eye Kits sold: ")
    return dry_eye

def get_tears():
    # TODO: Get input from user how many artificial tears were sold
    art_tears = utils.get_int("Enter the number of Artificial Tears sold: ")
    return art_tears

def display():
    # TODO: Display transaction for customer
    number_glasses = glasses.get_number_of_glasses()
    total_sale = glasses.get_total_sale()
    print()
    print(f"Total number of glasses: \t\t{number_glasses}")
    print(f"Total number of sun glasses: \t\t{number_suns}")
    print(f"Total number of kids glasses: \t\t{number_kid_glasses}")
    print(f"Total number of kids sun glasses: \t{number_kid_sun_glasses}")
    print(f"Total number of dry eye kits: \t\t{number_dry_eye}")
    print(f"Total number of artificial tear: \t{number_art_tears}")
    print(f"Your total for your items is: \t\t${total_sale:,.2f}")

menu = glasses.display_menu()
print(menu)
number_glasses = get_glasses()
number_suns = get_suns()
number_kid_glasses = get_kid_glasses()
number_kid_sun_glasses = get_kid_sun_glasses()
number_dry_eye = get_dry_eye()
number_art_tears = get_tears()
glasses.calculate(number_glasses, number_suns, number_kid_glasses, number_kid_sun_glasses, number_dry_eye, number_art_tears)
display()
