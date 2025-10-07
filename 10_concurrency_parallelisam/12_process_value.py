from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():   # ✅ Ensure only one process updates at a time
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)  # 'i' means integer, 0 is the starting value
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value: ", counter.value)



# 🧩 🔍 What’s Happening Here
#  1. Value('i', 0)
"""
- This creates a shared memory value that all processes can access.
- 'i' means it stores an integer (c_int type).
- The 0 is its initial value.
- Every process can read and write to this same counter variable — it’s not a copy, it’s shared.
"""

# 2. counter.get_lock()
"""
- Even though Value is shared, if multiple processes try to modify it at the same time, you can still get race conditions.
- So we use a lock (built into Value) to ensure that only one process updates counter.value at a time.
"""

# 3. Processes
"""
- 4 separate processes each run increment() 100,000 times.
- So, ideally, final value = 4 * 100000 = 400000
- Because of the lock, the counter increases safely and accurately.
"""



# ⚙️ Why We Use Value
"""
- We use Value when:
    - You just need to share a single variable (like a number, boolean, or small data structure).
    - You want direct shared memory access, not message passing.
- It’s faster and simpler for small shared data.
"""

# 🧋 Real-life Analogy
"""
Let’s say you have 4 waiters (processes) taking orders:

You use Queue if each waiter needs to hand over full orders to the chef — like “Tea, Coffee, Sandwich”.

You use Value if you just need to increment a single shared counter, like “How many customers have been served in total”.
"""