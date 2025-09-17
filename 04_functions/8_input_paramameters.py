# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ", order)


# prepare_chai(chai)
# print(chai)


chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keywords


# [args or arguments and *kwargs or keyword arguments] -> mix of both positional and keywords
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)  # return tuple
    print("Extras", extras) # return dictonary

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")

# [passing default value to parameters]

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# chai_order()
# chai_order()
# output = ["Masala","Masala"]

# [touble shoot above problem]

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order("Masala chai") # output: Masala chai
chai_order() # output: []


