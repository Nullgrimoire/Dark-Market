import threading
import time
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

market_prices = {
    "Dragonbone": 120,
    "Soul Ash": 85,
    "Aether Silk": 45,
    "Cursed Gem": 200
}

inventory = {
    "gold": 500,
    "Dragonbone": 0,
    "Soul Ash": 0,
    "Aether Silk": 0,
    "Cursed Gem": 0
}

def fluctuate_prices():
    while True:
        time.sleep(random.randint(5, 15))  # wait 5–15 seconds randomly
        for item in market_prices:
            change = random.randint(-15, 15)
            market_prices[item] = max(5, market_prices[item] + change)
        print("🌀 Market updated:", market_prices)

@app.route("/")
def index():
    return render_template("index.html", market=market_prices, inventory=inventory)

@app.route("/trade", methods=["POST"])
def trade():
    item = request.form["item"]
    action = request.form["action"]
    price = market_prices[item]

    if action == "buy" and inventory["gold"] >= price:
        inventory[item] += 1
        inventory["gold"] -= price
    elif action == "sell" and inventory[item] > 0:
        inventory[item] -= 1
        inventory["gold"] += price

    return redirect(url_for("index"))

if __name__ == "__main__":
    # Start the market updater in a background thread
    t = threading.Thread(target=fluctuate_prices, daemon=True)
    t.start()

    app.run(host="0.0.0.0", port=5000, debug=True)
