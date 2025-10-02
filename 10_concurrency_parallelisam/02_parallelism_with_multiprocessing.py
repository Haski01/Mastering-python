import time
import multiprocessing

# ---------------- Parallelism with Multiprocessing ----------------
def heavy_calculation(n):
    print(f"Calculating square of {n}...")
    time.sleep(2)  # Simulating heavy CPU work
    print(f"Square of {n} is {n*n}")

# Using multiprocessing (Parallelism)
def parallelism_example():
    start = time.time()

    # Two tasks running "in parallel" using multiple cores
    p1 = multiprocessing.Process(target=heavy_calculation, args=(5,))
    p2 = multiprocessing.Process(target=heavy_calculation, args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(f"⏱️ Parallelism total time: {end - start:.2f} sec\n")

# ---------------- RUN EXAMPLES ----------------
if __name__ == "__main__":
    parallelism_example()
