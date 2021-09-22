from Topping import Topping

class Pizza(object):
    def __init__(self, id, name, topping, price):
        self.Id = id
        self.Name = name
        self.Topping=topping
        self.Price = price

    def AddTopping (self, toppingName):
        self.Topping.Append(toppingName)    
     