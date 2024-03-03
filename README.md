# Python-OOP---Coffee-Machine
This repository presents and Object Oriented Programming (OOP) project coded in python. The code requirements are given alongside, feel free to code it yourself based on them and cross checking with mine.
Concepts - OOPS, Python OOPS, Abstraction, Encapsulation, modules
Difficulty - Easy

# Requirements:

The whole project is to comprise of 3 separate python modules located on the same folder, 2 of which should include class designs and a main.py module including the process flow of the whole program. 

## Module 1: coffeeMachine.py 

This module should include the definition of the class of CoffeeMachine. This class is to be defined according to the following design:

1. Initialization:
   * Initialize machine with default resources: 3000 mL water, 2000 mL milk, 500 g coffee, $0 money.
   * Prompt user with menu and prices.
   * Reset money inventory to $0.

2. User Interaction:
   2.1. Prompt user: "What would you like?"
   2.2. Secret codes: 'off' to turn off, 'report' for resource & cash report.

3. Report Functionality: Generate and display resource and cash report.
   * Format: Water - _ mL, Milk - _ mL, Coffee - _ mL, Money - _ $.

4. Resource Check: Check if sufficient resources for selected drink.
   * Print message if not enough items.
   * Wait 10 seconds if resource depleted.

5. Payment Handling:
   * Prompt user for payment, retry if incorrect.
   * Limit retries to 3 to prevent infinite loops, cancel order after.

6. Coffee Making:
   * Deduct ingredients from resources.
   * Dispense drink. Print a message conveying the same.
   
7. Maintenance Operations: Methods to add resources and clear money.

## Module 2: Menu.py

This module should include the definition of the class of MenuItem and Menu. These classes are to be defined according to the following designs:

1. MenuItem class:
   * Represents drink with name, cost, ingredients.
     
3. Menu class:
   * Initialize with menu items.
   * Display menu to customer.
   * Order function to get customer's choice.
     
5. Manintenance operations:
   * Add/remove menu items.
  
## Module 3: main.py

This module includes the process flow of the whole program. 

1. Import Modules:
   * coffeeMachine.py, Menu.py
     
3. Object Creation:
   * Create coffee machine and menu objects.
     
5. Main Loop:
   * Prompt user, handle orders.
   * Check resources after each order.
   * Shutdown if resources depleted.

I had a tough time to practice coding using OOP principles. So I thought, something like this is very needed, as this paradigm is heavily important for a software developer to master, to build scalable and robust software solutions. I am planning to work on more challenging projects along the same lines. Feel free to point out my design flaws or even appreciate them :)
