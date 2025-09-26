def chai_customer():
    print("Welcome! what type of chai would you like to prefer..")
    order = yield

    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala chai")
stall.send("Lemon chai")