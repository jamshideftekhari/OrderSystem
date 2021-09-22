import Pizza 
from Topping import Topping
class Persistent(object):
    PizzaList = []
    
    def __init__(self):
        TL1 = [Topping("Cheese"), Topping("Tomato"), Topping("Ham")]
        TL2 = [Topping("Cheese"), Topping("Tomato"), Topping("Ham"), Topping("Bacon")]
        TL3 = [Topping("Cheese"), Topping("Tomato"), Topping("Ham"), Topping("Bacon"),Topping("Olive")]
        

        self.PizzaList.append(Pizza.Pizza(1, "Margherita", TL1,50))
        self.PizzaList.append(Pizza.Pizza(2, "Naples", TL2,70))
        self.PizzaList.append(Pizza.Pizza(3, "Vesuvio", TL3,75))
        
    def GetPizza(self):
        return self.PizzaList

    def AddPizza(self, pizza):
        self.PizzaList.append(pizza)

    def SaveMenu(self):
        pass        
