import threading   # Importing threading module for concurrent execution
import time         # Importing time module to simulate delay

# Function to simulate boiling milk
def boil_milk():
    print("Boiling milk...")  
    time.sleep(2)              # Simulates the time taken to boil milk
    print("Milk Boiled...")

# Function to simulate toasting a bun
def toast_bun():
    print("Toasting bun...")
    time.sleep(3)              # Simulates the time taken to toast the bun
    print("Done with bun toast...")

# Record the start time
start = time.time()

# Creating two threads (each task runs concurrently)
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

# Starting both threads — they run at (almost) the same time
t1.start()
t2.start()

# Wait for both threads to finish before moving ahead
t1.join()
t2.join()

# Record the end time
end = time.time()

# Print total time taken
print(f"Breakfast is ready in {end - start:.2f} seconds")

"""
🧩 What This Code Does

-> This code shows how multithreading works in Python —
Both boil_milk() and toast_bun() run concurrently using threads.

- Normally, if you run them one after another (sequentially):
    - Boil milk → takes 2 seconds
    - Toast bun → takes 3 seconds
    - Total = 5 seconds

- But using multithreading, they run together:
    - Both tasks overlap in time
    - Total = about 3 seconds (the longest task dominates)
"""

"""
⚙️ What This Code Demonstrates

-> ➡️ Concept Shown:
    - This example demonstrates Concurrency using Threads — multiple tasks overlapping in time (best for I/O-bound tasks).

-> ➡️ Real-World Analogy:
    While milk is boiling, you’re also toasting a bun. You’re not waiting for one to finish before starting the other 🍞🥛
"""
