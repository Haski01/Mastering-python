import threading
import time

def preparing_chai(type_, wait_time):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} ready.")

start = time.time()

# Creating two threads for two different chai preparations
t1 = threading.Thread(target=preparing_chai, args=("Masala", 2))
t2 = threading.Thread(target=preparing_chai, args=("Ginger", 3))

# Starting both threads
t1.start()
t2.start()

# Waiting for both threads to complete
t1.join()
t2.join()

end = time.time()
print(f"Chai ready in {end - start:.2f} seconds")

"""
- The breakfast example shows: “Do two different things (milk + bun) at the same time.”

- The chai example shows: “Do the same kind of thing (make chai) twice with different ingredients and timing.”

comparition: Both use multithreading, but the second one adds a layer of flexibility — by passing arguments dynamically into the thread function.
"""