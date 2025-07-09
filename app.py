from flask import Flask, render_template, jsonify, request, redirect, url_for
import threading
import time
import random

app = Flask(__name__)

# Starting prices
market_prices = {
    "Dragon Bone": 150,
    "Soul Ash": 80,
    "Aether Silk": 50,
    "Cursed Gem": 200
}

inventory = {
    "Gold": 500,
    "Dragon Bone": 0,
    "Soul Ash": 0,
    "Aether Silk": 0,
    "Cursed Gem": 0
}

# Market news history (last 5 changes)
market_news = [
    "[*] A seer predicted a surge in Dragon Bone demand.",
    "[*] Short supply and high demand caused a Soul Ash price spike.",
    "[~] The value of Aether Silk remains unchanged.",
    "[~] The value of Cursed Gem remains unchanged."
]

# Major market events (name, {item: modifier})
MAJOR_EVENTS = [
    ("Elven civil war erupts!", {"Aether Silk": 0.5}),
    ("Necromancer rises in the East!", {"Soul Ash": 0.6}),
    ("Dragon Bone smuggling ring exposed!", {"Dragon Bone": 0.5}),
    ("Cursed Gem declared illegal!", {"Cursed Gem": -0.5}),
    ("Aether Silk market flooded!", {"Aether Silk": -0.4}),
    ("Dragon Bone shortage after mine collapse!", {"Dragon Bone": 0.7}),
    ("Soul Ash ritual backfires!", {"Soul Ash": -0.6}),
]

data_lock = threading.Lock()

# Price fluctuation logic (one item at a time)
def fluctuate_market():
    while True:
        time.sleep(5)

        with data_lock:
            # 1 in 15 chance for a major event
            if random.randint(1, 15) == 1:
                event, effects = random.choice(MAJOR_EVENTS)
                for item, modifier in effects.items():
                    base = market_prices[item]
                    change = round(base * modifier)
                    old_price = market_prices[item]
                    market_prices[item] = max(1, base + change)
                    news = f"[!] {event} {item} price {'rose' if change > 0 else 'fell'} by {abs(change)} gold."
                    market_news.append(news)
                    if len(market_news) > 5:
                        market_news.pop(0)
                continue  # skip normal fluctuation this cycle

            item = random.choice(list(market_prices.keys()))
            change = random.randint(-50, 50)

            old_price = market_prices[item]
            new_price = max(1, old_price + change)
            market_prices[item] = new_price

            # Debug logging
            print(f"Price change: {item} {old_price} -> {new_price} (change: {change:+d})")

            # Create news entry
            if change > 0:
                news = f"[^] {item} prices rose due to rising demand."
            elif change < 0:
                news = f"[v] {item} prices dropped after market surplus."
            else:
                news = f"[~] The value of {item} remains unchanged."
            market_news.append(news)
            # Keep only last 5 news
            if len(market_news) > 5:
                market_news.pop(0)

@app.route("/")
def index():
    item_order = ["Dragon Bone", "Soul Ash", "Aether Silk", "Cursed Gem"]
    return render_template("index.html", prices=market_prices, inventory=inventory, rumors=market_news, item_order=item_order)



@app.route("/api/market")
def api_market():
    with data_lock:
        data = {
            "prices": dict(market_prices),
            "inventory": dict(inventory),
            "rumors": list(market_news),
        }
    print(f"API call: Current prices: {data['prices']}")
    return jsonify(data)


@app.route("/trade/<action>/<item>", methods=["POST"])
def trade(action, item):
    item = item.title()
    data = request.get_json()
    quantity = data.get("quantity", 1)
    with data_lock:
        if item not in market_prices:
            return "Item not found", 400

        price = market_prices[item]
        if action == "buy":
            if quantity == "max":
                quantity = inventory["Gold"] // price
            else:
                quantity = int(quantity)
            total_cost = price * quantity
            if inventory["Gold"] >= total_cost and quantity > 0:
                inventory["Gold"] -= total_cost
                inventory[item] += quantity
        elif action == "sell":
            if quantity == "max":
                quantity = inventory[item]
            else:
                quantity = int(quantity)
            if inventory[item] >= quantity and quantity > 0:
                inventory["Gold"] += price * quantity
                inventory[item] -= quantity
    return ("", 204)

threading.Thread(target=fluctuate_market, daemon=True).start()
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
