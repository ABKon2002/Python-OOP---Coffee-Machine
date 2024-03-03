import coffeeMachine as machine
import Menu as menu

def main():
    mac = machine.CoffeeMachine()
    catalog = menu.Menu()

    flag = True
    while flag:
        print("\n-----------------------------------------------------------")
        print("Good day! We are happy to serve you..")
        print("-----------------------------------------------------------\n")
        order = mac.prompt(catalog)
        if order == -1:
            break
        elif order == True:
            continue
        mac.makeCoffee(order)
        
        for item in mac.resources:
            if mac.resources[item] <= 20:
                print(f"The machine ran out of {item}. Report it to maintenance!")
                flag = False
                break           # This part can be further enhanced by using the maintenance operations of the machine...


if __name__ == '__main__':
    main()
