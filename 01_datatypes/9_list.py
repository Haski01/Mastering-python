# [********************Python list datatype*******************]

# A list is an ordered, mutable collection of elements.
# Can hold different types of data (integers, strings, floats, objects).
# Defined using square brackets [] or list().


# [Creating Lists]

# Empty list
empty = []
print(empty)    # []

# List of numbers
nums = [1, 2, 3, 4, 5]
print(nums)     # [1, 2, 3, 4, 5]

# List with mixed data types
mixed = ["Asad", 21, 5.9, True]
print(mixed)    # ['Asad', 21, 5.9, True]

# Nested list (list inside a list)
nested = [[1, 2, 3], [4, 5, 6]]
print(nested)   # [[1, 2, 3], [4, 5, 6]]

# Using list() function
chars = list("Python")
print(chars)    # ['P', 'y', 't', 'h', 'o', 'n']



# [Accessing & Slicing Lists]

fruits = ["apple", "banana", "mango", "grapes"]

# Indexing
print(fruits[0])    # apple
print(fruits[-1])   # grapes

# Slicing
print(fruits[1:3])  # ['banana', 'mango']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[::2])  # ['apple', 'mango']


# [Lists are Mutable]

nums = [10, 20, 30]

# Changing value
nums[1] = 99
print(nums)   # [10, 99, 30]

# Adding new element
nums.append(40)
print(nums)   # [10, 99, 30, 40]


# [**************************List Operations********************]

# [Concatenation & Repetition]
a = [1, 2, 3]
b = [4, 5]

print(a + b)   # [1, 2, 3, 4, 5]
print(a * 2)   # [1, 2, 3, 1, 2, 3]


# [Membership Test]
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)      # True
print("orange" not in fruits) # True


# [Useful List Methods]
nums = [10, 20, 30, 40]

# Adding elements
nums.append(50)        # Add at end
nums.insert(1, 15)     # Insert at index 1
nums.extend([60, 70])  # Add multiple elements
print(nums)            # [10, 15, 20, 30, 40, 50, 60, 70]

# Removing elements
nums.remove(20)   # Remove first occurrence of 20
popped = nums.pop()    # Remove last element
print(popped)          # 70
del nums[0]            # Delete by index
print(nums)

# Searching
print(nums.index(30))  # 2 → index of element
print(nums.count(40))  # 1 → count of element

# Sorting
nums.sort()          # Ascending
nums.sort(reverse=True)  # Descending
print(nums)

# Copying
nums_copy = nums.copy()
print(nums_copy)

# Clearing list
nums.clear()
print(nums)   # []


# [Iterating Lists]

fruits = ["apple", "banana", "mango"]

# Using for loop
for fruit in fruits:
    print(fruit)

# Using enumerate (gives index + value)
for i, fruit in enumerate(fruits):
    print(i, fruit)


# [List Comprehension (Pythonic Way)]

# Generate squares
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

# Filtering
evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8]



