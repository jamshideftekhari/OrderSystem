from MenuType import MenuType
from Persistent import Persistent

class Menu(object):
    Pizzas=[]
    Drinks=[]
    Dessert=[]
    myMenu = Persistent()
    def __init__(self):
        self.Pizzas = self.myMenu.GetPizza()
    
    def AddPizza(self, pizza):
        self.myMenu.AddPizza(pizza) 

    def GetPizzaList(self):
        return self.Pizzas  

    def PrintMenuItem(self):
        print (MenuType.Pizza.name)
        for obj in self.Pizzas:
         print(obj.Id, obj.Name, obj.Price)
         toppings = ""
         for top in obj.Topping:
          toppings = toppings+" "+ top.ToppingName
         print ("Toppings: " + toppings)
      #  print (MenuType.ColdDrinks.name)
      #  for item in MenuType:
           # print(item.name)
