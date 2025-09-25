# Creates a new list by looping through an iterable.


# normal loop

square = []

for i in range(1, 5 + 1):
    square.append(i * i)

print(square)

# Using list comprehension

# example1
square_root = [i * i for i in range(1, 5 + 1) ]
print(square)

# example:2
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

ice_tea = [tea for tea in menu if "Iced" in tea]
print(ice_tea)
