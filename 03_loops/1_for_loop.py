# Python for loop

# A loop lets us repeat a block of code multiple times.
# In Python, for loops are used to iterate over a sequence (like list, tuple, string, dictionary, range, etc.).


# [Iterating Over a List]
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)


# [Iterating Over a String]
for char in "Python":
    print(char)


# [**************************Using range() in for Loop**********************]
# range() generates a sequence of numbers.

# range(start, stop, step)
for i in range(1,6,2): # start = 1, stop=5(6 not includid)   
    print(i)


