import time
import threading

def take_order():
    for i in range(1,4):
        print(f"Taking order for {i}")
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f"brewing chai for {i}")
        time.sleep(3)

# creat thread
t1 = threading.Thread(target=take_order)
t2 = threading.Thread(target=brew_chai)

# start thread
t1.start()
t2.start()

# # wait threads to finish task
t1.join()
t2.join()

