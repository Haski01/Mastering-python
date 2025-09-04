# A set is an unordered collection of unique elements.
# It automatically removes duplicates.
# Defined using {} or set().



# [Creating a Set]

fruits = {"apple", "banana", "mango", "apple"}  
print(fruits)   # Output: {'apple', 'banana', 'mango'}  → duplicate removed

# Empty set
empty_set = set()    # ✅ correct way
empty_dict = {}      # ❌ this creates a dictionary, not a set


# 3. Properties of Sets
#   - Unordered → No indexing, slicing, or order.
#   - Unique values only → Duplicates are not allowed.
#   - Mutable → We can add/remove elements.
#   - Elements must be immutable → You can store numbers, strings, tuples, but not lists or dicts.


# [Adding Elements]

fruits = {"apple", "banana"}
fruits.add("mango")     # adds one element
print(fruits)           # Output: {'apple', 'banana', 'mango'}

# Adding multiple elements
fruits.update(["grapes", "orange"])
print(fruits)   # Output: {'apple', 'banana', 'mango', 'grapes', 'orange'}


# [Removing Elements]

fruits = {"apple", "banana", "mango"}

fruits.remove("banana")    # removes item (❌ gives error if not found)
print(fruits)              # Output: {'apple', 'mango'}

fruits.discard("pineapple")  # safely removes (✅ no error if not found)
print(fruits)

fruits.pop()    # removes a random element
print(fruits)

fruits.clear()  # removes all elements
print(fruits)   # Output: set()


# [******************Set Operations*******************]

# Union (combine elements)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)            # Output: {1, 2, 3, 4, 5}
print(a.union(b))       # same as above


# Intersection (common elements)

print(a & b)            # Output: {3}
print(a.intersection(b)) # output same as above


# Difference (elements in A but not in B)

print(a - b)            # Output: {1, 2}
print(a.difference(b))

# Symmetric Difference (elements in A or B but not both)

print(a ^ b)            # Output: {1, 2, 4, 5}
print(a.symmetric_difference(b))

# Membership Test

fruits = {"apple", "banana", "mango"}
print("apple" in fruits)     # True
print("grapes" not in fruits)  # True


# Frozen Set (Immutable Set)
#   - Normal sets are mutable.
#   - If you need an immutable version, use frozenset().

fs = frozenset([1, 2, 3])
# fs.add(4)   # ❌ Error: frozenset cannot be changed
print(fs)     # Output: frozenset({1, 2, 3})


