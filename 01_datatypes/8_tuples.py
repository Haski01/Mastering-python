# [Python Tuple Datatype]

# A tuple is an ordered collection of items.
# Similar to a list, but immutable → cannot be changed after creation.
# Defined using () or tuple().


# [Creating Tuples]

# Normal tuple
t1 = (1, 2, 3, 4)
print(t1)          # (1, 2, 3, 4)

# Tuple with different data types
t2 = ("Asad", 21, True)
print(t2)          # ('Asad', 21, True)

# Nested tuple
t3 = (1, (2, 3), (4, 5))
print(t3)          # (1, (2, 3), (4, 5))

# Single element tuple (must have a comma!)
t4 = (10,)
print(type(t4))    # <class 'tuple'>

# Empty tuple
t5 = ()
print(type(t5))    # <class 'tuple'>




# [Accessing Elements]

numbers = (10, 20, 30, 40)

print(numbers[0])     # 10 → indexing
print(numbers[-1])    # 40 → negative indexing
print(numbers[1:3])   # (20, 30) → slicing


# [Immutability of Tuples]

t = (1, 2, 3)
# t[0] = 10   # ❌ Error: tuples are immutable

# But if tuple contains a mutable item, that can change
t = (1, [2, 3], 4)
t[1].append(5)
print(t)   # (1, [2, 3, 5], 4)


# [*********************Tuple Operations***********************]

# [Concatenation & Repetition]
a = (1, 2, 3)
b = (4, 5)

print(a + b)   # (1, 2, 3, 4, 5)
print(a * 2)   # (1, 2, 3, 1, 2, 3)


#[Membership Test]
fruits = ("apple", "banana", "mango")
print("apple" in fruits)     # True
print("grapes" not in fruits)  # True


# [Tuple Methods]
nums = (1, 2, 3, 2, 4, 2)

print(nums.count(2))   # 3 → counts how many times 2 appears
print(nums.index(3))   # 2 → index of first occurrence of 3

# [Tuple Unpacking]

person = ("Asad", 21, "BCA")

# unpacking tuple into variables
name, age, course = person
print(name)    # Asad
print(age)     # 21
print(course)  # BCA
