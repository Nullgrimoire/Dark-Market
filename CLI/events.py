import random

EVENTS = [
    ("Elven civil war erupts!", {"Elven Wine": 0.5}),
    ("Necromancer rises in the East!", {"Ectoplasm": 0.6}),
    ("Goblin invents lightning bolt battery!", {"Goblin Tech": 0.4}),
    ("Wyvern migration floods the market!", {"Wyvern Scales": -0.3}),
    ("Phoenix born anew in the highlands!", {"Phoenix Feather": -0.4}),
    ("Dragon Bone smuggling ring exposed!", {"Dragon Bone": 0.5}),
]

class EventManager:
    def __init__(self, market):
        self.market = market
        self.history = []

    def trigger_random_event(self):
        event, effects = random.choice(EVENTS)
        print(f"\n⚠️ EVENT: {event}")
        self.history.append(event)

        for item, modifier in effects.items():
            base = self.market.prices[item]
            change = round(base * modifier)
            self.market.prices[item] = max(1, base + change)
            print(f"{item} price adjusted by {change} gold.")

    def show_history(self):
        print("\n--- Recent World Events ---")
        if not self.history:
            print("No events yet.")
        else:
            for event in self.history[-5:]:
                print(f"- {event}")
