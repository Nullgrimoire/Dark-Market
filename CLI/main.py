from market import Market
from inventory import Player
from events import EventManager

def main():
    market = Market()
    player = Player()
    event_manager = EventManager(market)

    print("🧛‍♂️ Welcome to DARK MARKET 🧛‍♂️")
    print("Buy low, sell high, and survive the chaos.\n")

    while True:
        print("\n--- Market Summary ---")
        market.display_prices()
        print("\n--- Your Inventory ---")
        player.display()

        print("\n[1] Buy  [2] Sell  [3] Read News  [4] End Turn  [5] Quit")
        choice = input("Choose an action: ").strip()

        if choice == "1":
            player.buy_item(market)
        elif choice == "2":
            player.sell_item(market)
        elif choice == "3":
            event_manager.show_history()
        elif choice == "4":
            event_manager.trigger_random_event()
            market.update_prices()
        elif choice == "5":
            print("Farewell, merchant of shadows.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
