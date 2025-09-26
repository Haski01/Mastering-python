def local_chai():
    yield "Masala chai"
    yield "Ginger chai"

def impoted_chai():
    yield "Matcha"
    yield "Oolong"

def chai_menu():
    yield from local_chai()
    yield from impoted_chai()

# for chai in chai_menu():
#     print(chai)


def custome_chai():
    try:
        while True:
            print("Waiting for order!")
            order = yield 
            print(f"Preparing order: {order}")
            order = yield
    except:
        print("Stall close no more chai!")

chai = custome_chai()
next(chai) # start generator

chai.send("Masala chai")
chai.close() # close generator

# Quick Recap

'''
 - yield from → delegates iteration to another generator/iterable, cleaner than manual loops.
 - .close() → explicitly closes a generator, raising GeneratorExit.
'''