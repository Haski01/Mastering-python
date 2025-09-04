# [Python dictonary datatype]

# A dictionary is an unordered, mutable collection of key-value pairs.
# Keys must be unique and immutable (string, number, tuple).
# Values can be of any datatype.
# Defined using {} or dict().



# [Creating Dictionaries*********************]

# Empty dictionary
empty_dict = {}
print(empty_dict)    # {}

# Simple dictionary
student = {
    "name": "Asad",
    "age": 21,
    "course": "BCA"
}
print(student)

# Using dict() function
person = dict(name="Ali", age=25, city="Delhi")
print(person)

# Dictionary with mixed types
data = {1: "one", "two": 2, (3, 4): "tuple key"}
print(data)


# [Accessing Values**************************]

student = {"name": "Asad", "age": 21, "course": "BCA"}

# Access by key
print(student["name"])     # Asad

# Using get() (safer)
print(student.get("age"))  # 21
print(student.get("marks", "Not Found"))  # Not Found (default value)


# [Adding & Updating****************************]

student = {"name": "Asad", "age": 21}

# Adding new key-value
student["course"] = "BCA"

# Updating existing key
student["age"] = 22

print(student)  # {'name': 'Asad', 'age': 22, 'course': 'BCA'}


# [Removing Element********************]

student = {"name": "Asad", "age": 21, "course": "BCA"}

student.pop("age")     # Removes key 'age'
student.popitem()      # Removes last inserted item
del student["name"]    # Delete by key
student.clear()        # Removes all items

print(student)   # {}

# [************************Dictionary Methods************************]

student = {"name": "Asad", "age": 21, "course": "BCA"}

# Keys, Values, Items
print(student.keys())    # dict_keys(['name', 'age', 'course'])
print(student.values())  # dict_values(['Asad', 21, 'BCA'])
print(student.items())   # dict_items([('name', 'Asad'), ('age', 21), ('course', 'BCA')])

# Update dictionary
student.update({"age": 23, "city": "Delhi"})
print(student)


# [Iterating Dictionaries***************************]

student = {"name": "Asad", "age": 21, "course": "BCA"}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key} -> {value}")


# [Dictionary Comprehension***************************]

# Create square dictionary
squares = {x: x**2 for x in range(5)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)




# ✅ Quick Summary of Dictionaries

#   - Store data as key-value pairs.
#   - Keys must be unique & immutable.
#   - Mutable → can add, update, or delete.
#   - Useful in JSON, APIs, configs, and mapping relationships.
#   - Supports dictionary comprehension for quick creation.
