#                 [****************zip() in Python****************]

# 1. What is zip()?

#   - zip() is a built-in function that combines two or more iterables (like lists, tuples, strings) into a single iterable of tuples.
#   - Each tuple contains one element from each iterable at the same index.
#   - Stops at the shortest iterable (ignores extra items).




# Order summary

name = ["Asad","Meera","Sam","Ali"]
bill = [50,70,10,55]

for name, ammount in zip(name,bill):
    print(f"{name} paid {ammount} rupees")



# Practical Use Case – Dictionary Creation

keys = ["name", "age", "course"]
values = ["Asad", 21, "BCA"]

student = dict(zip(keys,values))
print(student)