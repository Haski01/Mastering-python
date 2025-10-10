import asyncio                    # For asynchronous programming (async/await)
import time                       # For simulating a blocking delay
from concurrent.futures import ThreadPoolExecutor   # For running blocking code in threads


# ------------------------------
# Normal (synchronous) function
# ------------------------------
def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3)  # Simulates a slow/blocking operation (like checking a database or API)
    return f"{item} stock: 42"   # Returns fake stock data


# ------------------------------
# Asynchronous function (coroutine)
# ------------------------------
async def main():
    # Get the current running event loop (it controls all async tasks)
    loop = asyncio.get_running_loop()

    # Create a thread pool (a group of threads to offload blocking work)
    with ThreadPoolExecutor() as pool:

        # Run the blocking function 'check_stock' in a separate thread
        # so that it doesn't block the main async loop.
        # 'loop.run_in_executor()' returns a coroutine that we can await.
        result = await loop.run_in_executor(pool, check_stock, "Masala chai")

        # Print the result after the blocking task completes
        print(result)


# ------------------------------
# Start the async event loop
# ------------------------------
asyncio.run(main())




# 🧠 What’s Happening Behind the Scenes

"""
- check_stock() is a normal blocking function — it uses time.sleep(3) (which halts the thread for 3 seconds).
    - Normally, this would freeze the whole async program if run directly.

- asyncio.get_running_loop() grabs the event loop that controls async execution.
- ThreadPoolExecutor() creates a pool of background threads.

- loop.run_in_executor(pool, check_stock, "Masala chai")
    → This runs the blocking function in one of those background threads.
    → The main async loop stays free and responsive.

- await waits for the thread to finish and then returns the result.
- Finally, the result is printed — "Masala chai stock: 42".
"""

# ☕ Real-life Analogy
"""
- Imagine you’re a shopkeeper managing many customers:
    - A customer asks you to check stock in the backroom (takes 3 mins).
    - Instead of going yourself and making other customers wait (blocking),
      you send a helper (thread) to check it for you while you serve others.

- That’s what run_in_executor() does — runs blocking work in another thread without pausing your async loop.
"""

