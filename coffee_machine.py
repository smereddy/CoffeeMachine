"""
Simulates an actual coffee machine! What do we need for that?
This coffee machine will have a limited supply of water, milk, coffee beans, and disposable cups.
Also, it will calculate how much money it gets for selling coffee.
"""


class Coffee:
    """
    Coffee class
    """

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
    
    def __update_cups(self):
        self.cups -= 1
    
    def __update_money(self, money):
        self.money += money

    def remaining(self):
        print()
        print("The coffee machine has:")
        print("{0} of water".format(self.water))
        print("{0} of milk".format(self.milk))
        print("{0} of coffee beans".format(self.beans))
        print("{0} of disposable cups".format(self.cups))
        print("{0} of money \n".format(self.money))
    
    def processing(self, milk, water, beans, money):
        self.water -= water
        if not self.water > 0:
            print("Sorry, not enough water!\n")
            return
        
        self.beans -= beans
        if not self.beans > 0:
            print("Sorry, not enough coffee beans!\n")
            return
        
        self.milk -= milk
        if not self.milk > 0:
            print("Sorry, not enough milk!\n")
            return
        
        print("I have enough resources, making you a coffee!\n")
        
        self.__update_cups()
        self.__update_money(money)


    def espresso(self):
        self.processing(water=250,beans=16,money=4,milk=0)

    def latte(self):
        self.processing(water=350,beans=20,milk=75,money=7)

    def cappuccino(self):
        self.processing(water=200,beans=12,milk=100,money=6)

    def actions(self):
        return input("Write action (buy, fill, take, remaining, exit):\n")

    def buy(self):
        type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if type == '1':
            self.espresso()
        elif type == '2':
            self.latte()
        elif type == '3':
            self.cappuccino()
        elif type == 'back':
            return
        else:
            print("Cannot process you order, invalid choice")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(
            input("Write how many grams of coffee beans do you want to add:")
        )
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("I gave you {0}".format(self.money))
        self.money = 0

if __name__ == "__main__":
    coffee = Coffee()
    while True:
        action = coffee.actions()
        if action != "exit":
            if coffee.cups <= 0:
                print("Sorry, not enough cups!")
                break
            getattr(coffee, action)()
        else:
            exit()
