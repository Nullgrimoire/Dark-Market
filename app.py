from flask import Flask, render_template, jsonify, request, redirect, url_for
import threading
import time
import random

app = Flask(__name__)

# Starting prices
market_prices = {
    "Dragonbone": 150,
    "Soul Ash": 80,
    "Aether Silk": 50,
    "Cursed Gem": 200
}

inventory = {
    "Gold": 500,
    "Dragonbone": 0,
    "Soul Ash": 0,
    "Aether Silk": 0,
    "Cursed Gem": 0
}

market_rumors = {
    "Dragonbone": "🔮 A seer predicted a surge in Dragonbone demand.",
    "Soul Ash": "🔥 Short supply and high demand caused a Soul Ash price spike.",
    "Aether Silk": "🔁 The value of Aether Silk remains unchanged.",
    "Cursed Gem": "🔁 The value of Cursed Gem remains unchanged."
}

data_lock = threading.Lock()

# Price fluctuation logic (one item at a time)
def fluctuate_market():
    while True:
        time.sleep(10)

        with data_lock:
            item = random.choice(list(market_prices.keys()))
            change = random.randint(-25, 25)

            old_price = market_prices[item]
            new_price = max(1, old_price + change)
            market_prices[item] = new_price

            # Update only that item's rumor
            if change > 0:
                market_rumors[item] = f"📈 {item} prices rose due to rising demand."
            elif change < 0:
                market_rumors[item] = (
                    f"📉 {item} prices dropped after market surplus."
                )
            else:
                market_rumors[item] = f"🌀 The value of {item} remains unchanged."
            # Reset others
            for other in market_prices:
                if other != item:
                    market_rumors[other] = (
                        f"🌀 The value of {other} remains unchanged."
                    )

@app.route("/")
def index():
    item_order = ["Dragonbone", "Soul Ash", "Aether Silk", "Cursed Gem"]
    return render_template("index.html", prices=market_prices, inventory=inventory, rumors=market_rumors, item_order=item_order)



@app.route("/api/market")
def api_market():
    with data_lock:
        data = {
            "prices": dict(market_prices),
            "inventory": dict(inventory),
            "rumors": dict(market_rumors),
        }
    return jsonify(data)


@app.route("/trade/<action>/<item>", methods=["POST"])
def trade(action, item):
    item = item.title()
    with data_lock:
        if item not in market_prices:
            return "Item not found", 400

        price = market_prices[item]

        if action == "buy":
            if inventory["Gold"] >= price:
                inventory["Gold"] -= price
                inventory[item] += 1
        elif action == "sell":
            if inventory[item] > 0:
                inventory["Gold"] += price
                inventory[item] -= 1
    return ("", 204)


if __name__ == "__main__":
    threading.Thread(target=fluctuate_market, daemon=True).start()
    app.run(debug=False, host="0.0.0.0", port=5000)
