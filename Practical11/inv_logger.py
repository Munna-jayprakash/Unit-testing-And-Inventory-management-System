import sys, importlib
# Safely import standard logging when file is named logging.py
sys.path = [p for p in sys.path if p not in ("", sys.path[0])]
logging = importlib.import_module("logging")
sys.path.insert(0, ".")

import inventory

logging.basicConfig(filename="application.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 1. Product checks
try:
    logging.info(f"Product check: {inventory.check_stock(10, 5)}")
    inventory.check_stock(5, 10)
except Exception as e:
    logging.error(f"Product check error: {e}")

# 2. Successful operations
try:
    total = inventory.calculate_total_price(100, 2)
    logging.info(f"Success: Total price is {total}")
    disc = inventory.apply_discount(total, 10)
    logging.info(f"Success: Discounted amount is {disc}")
except Exception as e:
    logging.error(f"Operation error: {e}")

# 3. Errors
try:
    inventory.calculate_total_price(-50, 2)
except Exception as e:
    logging.error(f"Calculation error: {e}")
