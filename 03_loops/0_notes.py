# Python for loop

# A loop lets us repeat a block of code multiple times.
# In Python, for loops are used to iterate over a sequence (like list, tuple, string, dictionary, range, etc.).

# What we learn through course
#   1. use for loop and while loop effectively
#   2. loop through sequence using range(),enumerate(), and zip()
#   3. Control loop behavior using "break", "continue", and "else" causes
#   4. ideentify when to use "for" vs "while" loop



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
for i in range(5):  
    print(i)


for i in range(1, 5, 2):  # start=2, stop=10, step=2
    print(f"using range: {i}")


# [Iterating with Index using enumerate()]

fruits = ["apple", "banana", "mango"]

for idx,fruit in enumerate(fruits):
    print( idx,fruit)

# [Iterating a Dictionary]

print("********Iterating a Dictionary***************")
student = {"name": "Asad", "age": 21, "course": "BCA"}

# Loop through keys
for key in student:
    print(f"Key: {key}")

# Loop through values
for value in student.values():
    print(f"Value: {value}")


# Loop through key-value pairs
for  key,value in student.items():
    print(f"Properties: {key} -> {value}")


# [Nested for Loops]

print("***************Nested loop***************")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# 8. Loop Control Statements

#   - break → exits loop immediately.
#   - continue → skips current iteration, moves to next.
#   - pass → placeholder, does nothing.

print("***************Loop control statement***************")

for i in range(5):
    if i == 3:
        break   # stops loop when i=3
    print(i)

for i in range(5):
    if i == 2:
        continue   # skip when i=2
    print(i)

for i in range(3):
    pass   # placeholder for future code


# ✅ Quick Summary of for Loop

#   - Used to iterate over sequences (list, tuple, string, dict, range).
#   - Supports indexing via enumerate().
#   - Can be nested.
#   - Supports break, continue, pass for control.
#   - With range(), acts like a traditional loop.






