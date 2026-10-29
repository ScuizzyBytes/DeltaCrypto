import threading
import time
from ApiClient import get_prices


def start_price_thread():
  def run():
    while True:
      try:
        get_prices()
      except Exception as e:
        print(f"Ошибка в потоке: {e}")

      time.sleep(5)

  thread = threading.Thread(target=run, daemon=True)
  thread.start()