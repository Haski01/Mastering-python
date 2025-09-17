# types of functions
# 1. pure vs impure
# 2. Recursive function
# 3. lambdas (also known as "Anonymous functions" when function does'nt have any name)

# pure function bcz it can not alter or disturb any ingredient globaly
def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended (impure function)
def impure_chai(cups):
    global total_chai
    total_chai += cups


# recursion
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1) # calling same function

print(pour_chai(3))


# lambda function
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))

print(strong_chai)