import multiprocessing
import time

# Task that simulates heavy CPU work
def cpu_task():
    print("Starting heavy calculation...")
    count = 0
    for i in range(10**7):  # CPU-bound loop
        count += i
    print("Finished calculation.")

# ---------------- Multiprocessing ----------------
def multiprocessing_example():
    start = time.time()
    p1 = multiprocessing.Process(target=cpu_task)
    p2 = multiprocessing.Process(target=cpu_task)
    p1.start(); p2.start()
    p1.join(); p2.join()
    end = time.time()
    print(f"⏱️ Multiprocessing time: {end - start:.2f} sec\n")

if __name__ == "__main__":
    multiprocessing_example()