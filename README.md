# 🧛‍♂️ Dark Market – A Fantasy Trading Simulator

Welcome to **Dark Market**, a fantasy trading simulator where you buy and sell magical commodities in a volatile world shaped by unpredictable lore events. Available in both **CLI** and **Web** modes!

Sharpen your instincts, interpret the signs, and manipulate the arcane markets to your advantage. Will you become the next Archmage Tycoon—or go bankrupt buying phoenix feathers?

## 🚀 Quick Start

Start the web version:
```bash
./run.sh
```

Or try the CLI version:
```bash
cd CLI && python3 main.py
```

## 🧙‍♂️ Features

- 💰 Trade magical items (different sets in Web and CLI modes)
- 🌪️ Random world events dynamically affect the economy each turn
- 📈 Market volatility keeps prices in constant flux
- 🧾 Track your inventory and balance while making strategic buys and sells
- 📜 Lore-driven event log immerses you in the ever-shifting world
- 🌐 **Web Interface**: Real-time trading with live price updates, retro pixel-art UI
- 🖥️ **CLI Mode**: Classic terminal-based gameplay with text menus

## 🛠️ Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Setup
1. Clone the repository:
```bash
git clone https://github.com/Nullgrimoire/dark-market.git
cd dark-market
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 How to Play

### Web Mode (Recommended)
Start the web server and open your browser:
```bash
./run.sh
# or manually:
flask run --host=0.0.0.0 --port=5000
```

Then visit `http://localhost:5000` in your browser.

### CLI Mode
For the classic terminal experience:
```bash
cd CLI
python3 main.py
```

### Gameplay
Each turn, you can:
1. View current market prices
2. Buy or sell items
3. Read the latest news events
4. End the turn to trigger a new event and update the market

Use gold wisely. Random events can spike or crash prices. Can you master the arcane art of fantasy economics?

## 📦 Available Items

**Note:** The available items differ between the Web and CLI versions.

### Web Version
| Item         | Base Price | Volatility |
|--------------|------------|------------|
| Dragon Bone  | 150 gold   | High       |
| Soul Ash     | 80 gold    | Medium     |
| Aether Silk  | 50 gold    | Low        |
| Cursed Gem   | 200 gold   | Extreme    |

### CLI Version
| Item            | Base Price | Volatility |
|-----------------|------------|------------|
| Wyvern Scales   | 50 gold    | High       |
| Ectoplasm       | 70 gold    | Very High  |
| Elven Wine      | 40 gold    | Low        |
| Phoenix Feather | 120 gold   | High       |
| Goblin Tech     | 90 gold    | Medium     |
| Dragon Bone     | 200 gold   | Extreme    |

## 🏗️ Project Structure

```
Dark-Market/
├── app.py              # Flask web application (Web mode)
├── CLI/                # Command-line interface (CLI mode)
│   ├── main.py         # CLI entry point
│   ├── market.py       # Market logic (CLI)
│   ├── inventory.py    # Player inventory system (CLI)
│   ├── events.py       # World events system (CLI)
│   └── Items.py        # Item definitions (CLI)
├── templates/          # HTML templates (Web)
│   └── index.html      # Main web interface
├── static/             # Static assets (Web)
│   ├── style.css       # Web styling
│   └── images/         # Images and icons
├── requirements.txt    # Python dependencies
├── run.sh              # Web server startup script
└── README.md           # This file
```

## 🔮 Planned Features

- ✨ Enhanced GUI with `rich` or `Textual`
- 📅 Turn-based calendar progression
- 🧠 AI rival traders
- 🗺️ Fantasy region generator for different economies
- 🧾 Exportable run summaries
- 📊 Trading statistics and charts
- 🎭 Character customization

## ❗ Known Limitations

- No persistent save system: Progress is lost when you exit.
- No user accounts or multiplayer.
- No automated test suite (ignore references to `test_project.py`).
- Web and CLI versions use different item sets and event logic.

## 🐛 Troubleshooting

**Flask not found**: Make sure you've activated the virtual environment and installed requirements:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**Port already in use**: Change the port in `run.sh` or kill the existing process:
```bash
lsof -ti:5000 | xargs kill -9
```

**Permission denied on run.sh**: Make it executable:
```bash
chmod +x run.sh
```

## 👑 Credits

**Project Lead:** Nullgrimoire
Inspired by D&D, tycoon games, and chaotic capitalism.

## 📜 License

MIT License. Use freely in your own arcane projects.

> "Buy low, enchant high." 🪄
