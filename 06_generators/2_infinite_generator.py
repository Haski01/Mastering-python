# example1

def infine_counter():
    start = 1
    while True:
        yield start
        start += 1

gen = infine_counter()
# print(next(gen)) # 1
# print(next(gen)) # 2

gen_test_using_loop = infine_counter()

# for _ in range(3):
#     print(next(gen_test_using_loop))

# example2

def infinite_refilling_chai():
    count = 1
    while True:
        yield f"Refil {count}"
        count += 1

refill_chai = infinite_refilling_chai()
for _ in range(5):
    print(next(refill_chai))

