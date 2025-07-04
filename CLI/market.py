import random
from Items import ITEMS

class Market:
    def __init__(self):
        self.prices = {item: data["base_price"] for item, data in ITEMS.items()}

    def update_prices(self):
        for item, data in ITEMS.items():
            change = random.uniform(-1, 1) * data["volatility"] * data["base_price"]
            self.prices[item] = max(1, round(self.prices[item] + change))

    def display_prices(self):
        for item, price in self.prices.items():
            print(f"{item}: {price} gold")
