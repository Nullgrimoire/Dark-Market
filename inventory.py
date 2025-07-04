class Player:
    def __init__(self):
        self.gold = 500
        self.inventory = {}

    def display(self):
        print(f"Gold: {self.gold}")
        for item, amount in self.inventory.items():
            print(f"{item}: {amount}")

    def buy_item(self, market):
        item = input("What do you want to buy? ").strip().title()
        if item not in market.prices:
            print("That item doesn't exist.")
            return

        price = market.prices[item]
        amount = int(input(f"How many {item}s? "))
        total = price * amount

        if self.gold >= total:
            self.gold -= total
            self.inventory[item] = self.inventory.get(item, 0) + amount
            print(f"Bought {amount} {item}(s) for {total} gold.")
        else:
            print("Not enough gold.")

    def sell_item(self, market):
        item = input("What do you want to sell? ").strip().title()
        if item not in self.inventory or self.inventory[item] == 0:
            print("You don't own any of that.")
            return

        amount = int(input(f"How many {item}s to sell? "))
        if amount > self.inventory[item]:
            print("You don't have that many.")
            return

        total = market.prices[item] * amount
        self.gold += total
        self.inventory[item] -= amount
        print(f"Sold {amount} {item}(s) for {total} gold.")
