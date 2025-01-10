import sys

class VendingMachine:
    def __init__(self):
        self.items = []  # List to store available items
        self.prices = []  # List to store corresponding prices
        self.amount = 0.0  # User's current balance

    def display_items(self):
        """Displays the items and their prices."""
        print("Available items:")
        for i, (item, price) in enumerate(zip(self.items, self.prices), start=1):
            print(f"{i}. {item} - ${price:.2f}")
        print()

    def insert_money(self):
        """Allows the user to insert money into the vending machine."""
        try:
            cash = float(input("Insert money (e.g., 5 for $5.00): ").strip())
            self.amount += cash
            print(f"You inserted ${cash:.2f}. Your total balance is now ${self.amount:.2f}.\n")
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")

    def buy_item(self):
        """Allows the user to buy an item."""
        if self.amount <= 0:
            print("Your current balance is $0.00. Please insert money first.\n")
            return

        try:
            choice = int(input("Enter the item number you want to buy: ").strip())
            if 1 <= choice <= len(self.items):
                item = self.items[choice - 1]
                price = self.prices[choice - 1]

                if self.amount >= price:
                    self.amount -= price
                    print(f"You bought {item} for ${price:.2f}. Your remaining balance is ${self.amount:.2f}.\n")
                    # Remove the purchased item
                    self.items.pop(choice - 1)
                    self.prices.pop(choice - 1)
                else:
                    print(f"Insufficient balance. {item} costs ${price:.2f}, but you only have ${self.amount:.2f}.\n")
            else:
                print("Invalid item number. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a valid item number.\n")

    def return_change(self):
        """Returns the remaining balance to the user."""
        print(f"Returning ${self.amount:.2f} in change. Thank you for using the vending machine!\n")
        self.amount = 0.0

    def add_items(self):
        """Adds items and their prices to the vending machine."""
        food = ["Chips", "Soda", "Candy", "Water"]
        money = [1.00, 5.00, 0.50, 1.00]

        for f, m in zip(food, money):
            self.items.append(f)
            self.prices.append(m)


def main():
    vending_machine = VendingMachine()
    vending_machine.add_items()

    while True:
        print("Welcome to the Vending Machine!")
        vending_machine.display_items()

        print("Options:")
        print("1. Insert money")
        print("2. Buy an item")
        print("3. Return change and exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            vending_machine.insert_money()
        elif choice == "2":
            vending_machine.buy_item()
        elif choice == "3":
            vending_machine.return_change()
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
