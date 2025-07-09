from market import Market
from inventory import Player
from events import EventManager

def show_help():
    print("\n=== DARK MARKET HELP ===")
    print("Commands:")
    print("  1 - Buy items from the market")
    print("  2 - Sell items from your inventory")
    print("  3 - Read recent world events")
    print("  4 - End turn (triggers new events)")
    print("  5 - Quit the game")
    print("  h - Show this help")
    print("\nTips:")
    print("- Watch for world events that affect prices")
    print("- Buy low, sell high!")
    print("- Some items are more volatile than others")

def main():
    market = Market()
    player = Player()
    event_manager = EventManager(market)

    print("🧛‍♂️ Welcome to DARK MARKET 🧛‍♂️")
    print("Buy low, sell high, and survive the chaos.")
    print("Type 'h' for help or '5' to quit.\n")

    while True:
        print("\n--- Market Summary ---")
        market.display_prices()
        print("\n--- Your Inventory ---")
        player.display()

        print("\n[1] Buy  [2] Sell  [3] Read News  [4] End Turn  [5] Quit  [h] Help")
        choice = input("Choose an action: ").strip().lower()

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
        elif choice == "h":
            show_help()
        else:
            print("Invalid choice. Type 'h' for help.")

if __name__ == "__main__":
    main()
