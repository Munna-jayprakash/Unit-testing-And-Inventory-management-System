# Practical 11 - Inventory Logging & Testing

This project demonstrates inventory management functions in Python along with automated tests and logging for product checks, operations, and errors.

---

## macOS Setup Instructions

### 1. Open Terminal and Navigate to the Project Directory
```bash
cd ~/Documents/Python_practical/Practical11
```

### 2. Verify Python Installation
Ensure Python 3 is installed:
```bash
python3 --version
```

### 3. (Optional) Set Up and Activate a Virtual Environment
If you prefer using a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
Install `pytest` (and `ruff` if needed for linting):
```bash
pip install pytest ruff
```

---

## Execution Instructions

### Run the Logging Script
Execute `logging.py` to record product checks, successful operations, and errors into `application.log`:
```bash
python3 logging.py
```
*(or `python logging.py` if your environment alias points to Python 3)*

### View the Generated Logs
To inspect the output logged to `application.log`:
```bash
cat application.log
```
Or view the most recent logs in real time:
```bash
tail -n 20 application.log
```

### Run the Inventory Script Directly
```bash
python3 inventory.py
```

### Run the Unit Tests
Execute the test suite using pytest:
```bash
pytest inventory_test.py
```

