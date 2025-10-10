"""
this example shows how you can combine asyncio with ProcessPoolExecutor to offload CPU-heavy work to another process while keeping your main program responsive.
"""

import asyncio
from concurrent.futures import ProcessPoolExecutor

# ------------------------------
# A normal (CPU-bound) function
# ------------------------------
def encrypt(data):
    return f"🔒 {data[::-1]}"


# ------------------------------
# Asynchronous main coroutine
# ------------------------------
async def main():
    # Get the current running event loop (manages async tasks)
    loop = asyncio.get_running_loop()

    # Create a pool of separate processes (not threads)
    # This is useful for CPU-heavy tasks, so each process can use its own CPU core
    with ProcessPoolExecutor() as pool:

        # Run the blocking CPU-heavy function in a separate process
        # 'loop.run_in_executor()' submits the task to the process pool
        # It returns a coroutine that we can await
        result = await loop.run_in_executor(pool, encrypt, "credit_card_1234")

        print(f"{result}")

# ------------------------------
# Entry point — run the async main function
# ------------------------------
if __name__ == "__main__":
    asyncio.run(main())
