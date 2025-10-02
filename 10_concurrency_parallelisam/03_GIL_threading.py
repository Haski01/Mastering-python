import threading
import time

# Task that simulates heavy CPU work
def cpu_task():
    print("Starting heavy calculation...")
    count = 0
    for i in range(10**7):  # CPU-bound loop
        count += i
    print("Finished calculation.")

# ---------------- Multithreading ----------------
def threading_example():
    start = time.time()
    t1 = threading.Thread(target=cpu_task)
    t2 = threading.Thread(target=cpu_task)
    t1.start(); t2.start()
    t1.join(); t2.join()
    end = time.time()
    print(f"⏱️ Multithreading time: {end - start:.2f} sec\n")

if __name__ == "__main__":
    threading_example()
