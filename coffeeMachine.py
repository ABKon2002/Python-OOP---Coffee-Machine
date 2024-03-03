import time

class CoffeeMachine:
    def __init__(self, water = 3000, milk = 2000, coffee = 500):
        self.resources = {'water' : water, 
                          'milk' : milk, 
                          'coffee' : coffee}
        self.inventory = 0
    
    def __str__(self):
        return f'''Resources left:
              Water ==> {self.resources['water']} mL
              Milk ==> {self.resources['milk']} mL
              Coffee ==> {self.resources['coffee']} g
              Inventory : {self.inventory} $'''
    
    def prompt(self, menu):
        menu.Display()
        order = menu.Order()
        if order == 'off':   # For turning off the machine / secret code for maintainers.
            print("Machine turning off...")
            self.report()
            return -1
        if order == 'report':
            self.report()
            return True
        return order
    
    def report(self):
        print(self)
    
    def check(self, drink):
        for ingredient in drink.ingredients:
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                print("Sorry, Not enough items! Report it to maintenance.")
                time.sleep(10)
                return False
        return True
    
    def pay(self, drink, turn = 0):
        payment = float(input(f"Please pay {drink.cost} to proceed: "))
        if drink.cost == payment:
            print(f"We are brewing delicious {drink.name}. Please wait...")
            self.inventory += payment
            return True
        print(f"Please pay exact amount to proceed. Transaction failed!")
        if turn <= 3:
            return self.pay(drink, turn+1)
        else:
            print("Order Cancelled! Please make way for the next person in queue.")
            return False
    
    def makeCoffee(self, drink):
        if self.check(drink) and self.pay(drink):
            time.sleep(5) 
            for ingedient in drink.ingredients:
                self.resources[ingedient] -= drink.ingredients[ingedient]
            print(f"Here is your {drink.name}! Enjoy your day..")
            time.sleep(5)


    
    # Maintenance Operations
    
    def add_milk(self, milk = 1000):
        self.resources['milk'] += milk
    
    def add_water(self, water = 1500):
        self.resources['water'] += water
    
    def add_coffee(self, coffee = 250):
        self.resources['coffee'] += coffee
    
