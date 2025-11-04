"""
Inventory management system with proper logging, validation, and secure coding practices.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Add items to stock safely."""
    if logs is None:
        logs = []
    if not isinstance(item, str):
        logging.warning(f"Invalid item name: {item}")
        return
    if not isinstance(qty, int):
        logging.warning(f"Invalid quantity type for item {item}: {qty}")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """Remove items safely, with specific exception handling."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.error(f"Item '{item}' not found in stock.")

def get_qty(item):
    """Return the quantity of an item."""
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Load inventory data from JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning("Inventory file not found. Starting with empty stock.")
        stock_data = {}

def save_data(file="inventory.json"):
    """Save inventory data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=2)

def print_data():
    """Print the full inventory report."""
    print("\n--- Inventory Report ---")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")

def check_low_items(threshold=5):
    """Return list of items below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]

def main():
    """Main demonstration function."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()
