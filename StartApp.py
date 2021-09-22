from typing import Match
from MenuType import MenuType
from Menu import Menu
from Topping import Topping
from Pizza import Pizza

MyMenu = Menu()
def ShowMenu():
 print(" ****** Basic Menu Items ***** ")
 MyMenu.PrintMenuItem()

def AddShowMenu():
 toppings = [Topping("Cheese"), Topping("Tomato"), Topping("Ham"), Topping("Mashroom")]
 pizza = Pizza(4, "Capriccosa", toppings,50)
 MyMenu.AddPizza(pizza)
 print(" ****** New Menu Items ***** ")
 MyMenu.PrintMenuItem()


keyInput = input( "press M for Menu and O to place an Order, q for quite " ) 
while keyInput != "q":
    if keyInput == "M":
        ShowMenu()
    elif keyInput == "O":
        AddShowMenu()   
    keyInput = input("press M for Menu and O to place an Order, q for quite ")


print(" Done ")
