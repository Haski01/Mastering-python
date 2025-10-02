import time
import threading

# ---------------- Concurrency with Threading ----------------
def make_tea(name):
    print(f"{name} started brewing tea...")
    time.sleep(2)  # Simulates waiting for water to boil (I/O wait)
    print(f"{name} finished brewing tea!")

# Using threading (Concurrency)
def concurrency_example():
    start = time.time()

    # Two tasks running "concurrently"
    t1 = threading.Thread(target=make_tea, args=("Masala Chai",))
    t2 = threading.Thread(target=make_tea, args=("Ginger Chai",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()
    print(f"⏱️ Concurrency total time: {end - start:.2f} sec\n")

concurrency_example()
