
class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost 
        self.ingredients = {'water' : water,
                            'milk' : milk, 
                            'coffee' : coffee}

class Menu:
    def __init__(self):
        self.items = {'es' : MenuItem('Espresso', 1.5, 50, 0, 18), 
                      'lt' : MenuItem('Latte', 2.5, 200, 150, 24), 
                      'cp' : MenuItem('Cappuccino', 3.0, 250, 50, 24)}

    def __str__(self):
        Menu = "Today's Menu:\n"
        for item in self.items.values():
            Menu += item.name
            Menu += ' '
            for i in range(40 - len(item.name)):
                Menu += '-'
            Menu += ' '
            Menu += str(item.cost)
            Menu += '\n'
        Menu += "Enjoy your Coffee!"
        return Menu

    def Display(self):
        print(self)

    def Order(self, turn = 0):
        choices = self.items.keys()
        print("Choices ==> " , end= ' ')
        print(choices)
        order = input("Order your Choice: ")
        if order == 'off' or order == 'report':
            return order
        elif order not in choices and turn <= 3:
            print("We dont serve this yet :( Try again.")
            self.Order(turn + 1)
        elif turn > 3:
            print("Order Cancelled! Please make way for the next person in queue.")
            return False
        else:
            return self.items[order]
    
    # Maintenance Operations:
    
    def addItem(self):
        name = input("Name: ")
        cost = float(input("Cost: "))
        print("Ingredients: ")
        water = int(input("Water ==> "))
        milk = int(input("Milk ==> "))
        coffee = int(input("Coffee ==> "))
        ab = input("Abbreviation: ")
        while ab in self.abbs:
            ab = input("Another abbreviation: ")
        self.items.append(MenuItem(name, cost, water, milk, coffee))
        self.abbs.append(ab)
    