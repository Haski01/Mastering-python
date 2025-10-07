"""
- This example is super important — it explains one of the most common problems in multithreading:
- 👉 Race conditions, and how to prevent them using a Lock 🔒
"""

# Goal of This Code
"""
- We want to increase a shared counter (a global variable) from multiple threads at the same time.
- This is a classic example to show data inconsistency problems that can happen when multiple threads modify the same variable simultaneously.
"""

import threading
import time

counter = 0
lock = threading.Lock()

def increase_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

start = time.time()
threads = [threading.Thread(target=increase_counter) for _ in range(5)]

[t.start() for t in threads]
[t.join() for t in threads]

end = time.time()
print(f"Final counter: {counter}")
print(f"Process completed in {end-start:.2f} seconds")

"""
[Race Condition]: When multiple threads modify shared data at once, causing wrong results.
[Lock]: Prevents race conditions by allowing only one thread at a time to access a resource.
[with lock]: Safely acquires and releases lock automatically.
"""