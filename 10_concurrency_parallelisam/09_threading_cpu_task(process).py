import threading
import time

def cpu_heavy_task_using_threading():
    print("Starting crunching number...")
    total = 0

    for i in range(10**7):
        total += i
    print("DONE ✅")

start = time.time()

threads = [threading.Thread(target=cpu_heavy_task_using_threading) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

end = time.time()
print(f"task done in {end-start:.2f} seconds")

# 🔍 Key Concept
"""
- This code uses threads to run two cpu_heavy() tasks simultaneously.
- However, because of the GIL (Global Interpreter Lock) in Python,
only one thread can execute Python bytecode at a time, even on a multi-core CPU.
"""

# 🧩 So what happens here:
"""
- Both threads are created, but only one can actually crunch numbers at a time.
- The CPU-bound work (for i in range(10**7)) keeps the GIL locked for long periods.
- As a result, you don’t see a big speed-up — it’s almost as slow as running one function twice.
"""

# 📉 Problem:
"""
- Multithreading doesn’t work efficiently for CPU-heavy tasks due to the GIL.
"""