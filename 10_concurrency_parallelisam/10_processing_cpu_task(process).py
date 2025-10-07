from multiprocessing import Process
import time

def cpu_heavy_task_using_threading():
    print("Starting crunching number...")
    total = 0

    for i in range(10**7):
        total += i
    print("DONE ✅")

if __name__ == "__main__":
    start = time.time()

    threads = [Process(target=cpu_heavy_task_using_threading) for _ in range(2)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    end = time.time()
    print(f"task done in {end-start:.2f} seconds")

# 🔍 Key Concept

"""
- This code uses separate processes, not threads.

- Each process has:
    - Its own Python interpreter
    - Its own memory space
    - Its own GIL
"""

'''
✅ So now, each process runs truly in parallel — for example, one process on CPU core 1, another on CPU core 2.
'''

#  ⚔️ Difference Between multithreading vs multiprocessing
"""
| Feature                           | Multithreading              | Multiprocessing                                          

| **Library Used**                  | `threading`                   | `multiprocessing`
                                    
| **Memory**                        | Shared memory (same process space)    | Separate memory for each process 

| **GIL (Global Interpreter Lock)** | Affects performance — only one thread runs at a time   | Not affected — each process has its own GIL            |

| **Best For**                      | I/O-bound tasks (e.g., downloading files, network calls) | CPU-bound tasks (e.g., calculations, image processing) |

| **Overhead**                      | Lightweight (fast to start)   | Heavy (needs to create newprocesses) |

| **True Parallelism**              | ❌ No (GIL prevents it)               | ✅ Yes (each process runs independently)      
"""