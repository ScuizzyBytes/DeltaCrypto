# Crypto Coingecko Tracker

A lightweight desktop application built with Python and CustomTkinter for tracking cryptocurrency prices in real-time. The application fetches market data asynchronously from the Binance API using multi-threading to ensure a smooth, non-blocking GUI experience.

---

## Features

- **Real-Time Data**: Tracks prices for **BTC**, **ETH**, **BNB**, and **TON**.
- **Non-Blocking Interface**: API calls are executed in a separate background thread (`threading`) with recurring UI refreshes via CustomTkinter's `.after()` loop.
- **Data Validation**: Validates incoming price data types before UI formatting to prevent runtime exceptions during network reloads.
- **Modular Code Architecture**: Separated concerns across dedicated files (`main.py`, `ApiClient.py`, and `price_updater.py`).

---

## File Structure

```text
├── main.py            # CustomTkinter GUI layout and loop
├── ApiClient.py       # Fetching data from Binance REST API and state dictionary
└── price_updater.py   # Background thread runner for updating prices
```

---

## Requirements & Dependencies

- Python 3.8+
- `customtkinter`
- `requests`

### Installation

1. **Clone or download** the repository to your local machine.
2. **Install dependencies**:
   ```bash
   pip install customtkinter requests
   ```

---

## Usage

To start the tracker, run `main.py`:

```bash
python main.py
```

---

## Technical Details

- **API Endpoint**: Binance REST API (`/api/v3/ticker/price`).
- **Update Frequency**: Background API thread refreshes data every 5 seconds; the GUI polls internal state every 1 second.
- **State Management**: Shared dictionary state pattern between background threads and the primary Tkinter main loop.
