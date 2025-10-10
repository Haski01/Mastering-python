"""
This script demonstrates how to use threading (with a daemon thread)
alongside asyncio to perform background logging while running async tasks.

- A background thread continuously logs system health.
- Meanwhile, an async task simulates fetching orders after a delay.
"""

import asyncio
import threading
import time


# 🧠 Background worker function — runs continuously in a separate thread
def background_worker():
    """Continuously logs system health every second."""
    while True:
        time.sleep(1)  # Simulate a time delay for the logging cycle
        print("🕰️ Logging the system health...")


# 🎁 Async function — simulates fetching orders asynchronously
async def fetch_orders():
    """Simulates an asynchronous network operation (like fetching orders)."""
    await asyncio.sleep(3)  # Simulate a delay (like API call)
    print("✅ Orders fetched successfully!")


# 🚀 Main execution block
if __name__ == "__main__":
    # Start the background thread
    # daemon=True ➜ thread will stop automatically when main program exits
    threading.Thread(target=background_worker, daemon=True).start()

    # Run the async function
    asyncio.run(fetch_orders())

    # After async task completes, the program exits.
    # Since daemon=True, the background thread stops automatically.
