class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")

    def make_coffee(self, water = 0, milk = 0, beans = 0, cups = 0, cost = 0):
        if self.water >= water:
            self.water -= water
        else:
            print("Sorry, not enough water!")
            return

        if self.milk >= milk:
            self.milk -= milk
        else:
            print("Sorry, not enough milk!")
            return

        if self.beans >= beans:
            self.beans -= beans
        else:
            print("Sorry, not enough beans!")
            return

        if self.cups >= cups:
            self.cups -= cups
        else:
            print("Sorry, not enough cups!")
            return
        
        print("I have enough resources, making you a coffee!")
        self.money += cost

    def buy(self):
        flavor = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if flavor == "1":
            self.make_coffee(water=250, beans=16, cups=1, money=4) # milk=0
        elif flavor == "2":
            self.make_coffee(350, 75, 20, 1, 7)
        elif flavor == "3":
            self.make_coffee(200, 100, 12, 1, 6)

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print("I gave you " + str(self.money))
        self.money = 0

def main():
    coffe_machine = CoffeeMachine(water=400, milk=540, beans=120, cups=9, money=550)
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == "buy":
            coffe_machine.buy()
        elif action == "fill":
            coffe_machine.fill()
        elif action == "take":
            coffe_machine.take()
        elif action == "remaining":
            coffe_machine.remaining()
        elif action == "exit":
            break
        else:
            pass

if __name__ == "__main__":
    main()
