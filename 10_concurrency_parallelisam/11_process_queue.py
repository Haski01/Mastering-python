from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala chai is ready")

if __name__ == '__main__':
    queue = Queue()  # Create a shared queue that can be accessed by multiple processes

    p = Process(target=prepare_chai, args=(queue,))  # Pass the queue to the child process
    p.start()   # Start the new process
    p.join()    # Wait for the process to complete

    print(queue.get())  # Get the data that was added to the queue


# 🧾 Why We Use Queue
"""
✅ Problem:
- Each process in multiprocessing has its own separate memory — they can’t share variables directly.

💡 Solution:
- We use multiprocessing.Queue to send messages or data between processes safely.

- It’s a thread/process-safe data structure that:
    - Lets one process put() data into it.
    - Lets another process get() that data out.
"""

# 🧩 Real-World Analogy
"""
- Imagine you’re managing a tea shop ☕:
    - The main process is the cashier 🧾.
    - The child process is the chai maker 👨‍🍳.

- The Queue is the counter between them:

    - The chai maker puts the cup of tea on the counter (queue.put()).
    - The cashier picks it up and serves the customer (queue.get()).

They don’t share the same kitchen or workspace — the counter (Queue) is the only way to pass things safely.
"""
