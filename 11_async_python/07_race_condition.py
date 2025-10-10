#  🏁 Race Condition (Simple Meaning):

"""
- A race condition happens when two or more threads or processes try to access and modify the same data at the same time, and the final result depends on who “wins the race” to access that data first.
"""

# 💡 Real-world analogy:
"""
- Imagine you and your friend are both writing on the same whiteboard at the same time.

    - You’re trying to write “HELLO”
    - Your friend is trying to write “BYE”

- Both of you are racing to write — the letters get mixed up, and the final word becomes nonsense like “HEYBLLOE.” 😅
- 👉 That’s a race condition — when shared data gets messed up because multiple people (or threads) modify it simultaneously without coordination (lock).
"""

import threading

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [ threading.Thread(target=restock) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

print("Chai stock: ", chai_stock)