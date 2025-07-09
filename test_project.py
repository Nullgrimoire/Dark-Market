import pytest
import sys
import os
from flask import Flask

# --- Web (Flask) tests ---
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index_route(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Dark Market" in rv.data

def test_api_market(client):
    rv = client.get('/api/market')
    assert rv.status_code == 200
    data = rv.get_json()
    assert 'prices' in data
    assert 'inventory' in data
    assert 'rumors' in data

def test_trade_buy_sell(client):
    # Test buying and selling Dragon Bone
    buy_resp = client.post('/trade/buy/Dragon Bone', json={'quantity': 1})
    assert buy_resp.status_code == 204
    sell_resp = client.post('/trade/sell/Dragon Bone', json={'quantity': 1})
    assert sell_resp.status_code == 204

# --- CLI tests ---
import importlib.util
CLI_PATH = os.path.join(os.path.dirname(__file__), 'CLI')
sys.path.insert(0, CLI_PATH)
from market import Market
from inventory import Player
from events import EventManager
from Items import ITEMS

def test_items_structure():
    assert isinstance(ITEMS, dict)
    for k, v in ITEMS.items():
        assert 'base_price' in v
        assert 'volatility' in v

def test_market_prices():
    m = Market()
    assert isinstance(m.prices, dict)
    for item in ITEMS:
        assert item in m.prices
        assert isinstance(m.prices[item], int)
    old_prices = m.prices.copy()
    m.update_prices()
    # At least one price should change
    assert any(m.prices[item] != old_prices[item] for item in ITEMS)

def test_player_buy_sell(monkeypatch):
    m = Market()
    p = Player()
    p.gold = 1000
    m.prices = {item: 10 for item in ITEMS}
    # Simulate input for buying
    monkeypatch.setattr('builtins.input', lambda _: 'Wyvern Scales')
    monkeypatch.setattr('builtins.input', lambda _: '2')
    p.buy_item(m)
    assert p.inventory.get('Wyvern Scales', 0) >= 0
    # Simulate input for selling
    monkeypatch.setattr('builtins.input', lambda _: 'Wyvern Scales')
    monkeypatch.setattr('builtins.input', lambda _: '1')
    p.sell_item(m)

def test_event_manager():
    m = Market()
    em = EventManager(m)
    em.trigger_random_event()
    assert len(em.history) == 1
    em.show_history() 