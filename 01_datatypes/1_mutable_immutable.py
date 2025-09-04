# What are Data Types? -> Data types define the kind of value a variable can hold.

x = 10       # Integer type
name = "Asad"  # String type

# *****************Mutable vs Immutable Data Types******************
# Mutable: Can be changed/modified after creation.
# Immutable: Cannot be changed after creation. If modified, a new object is created.

# Immutable Example (String)
name = "Asad"
print(id(name))   # memory address
name = name + " Khan"
print(id(name))   # new memory address (new object created)

# Mutable Example (List)
fruits = ["apple", "banana"]
print(fruits) # ['apple', 'banana']
print(id(fruits))

fruits.append("mango")   # modifying the same list
print(fruits) # ['apple', 'banana', 'mango']
print(id(fruits))        # memory address remains same

# **********************Common Immutable and Immutable Data Types************
# Immutable: integers,strings,typles
# Mutable: list/array, dictionaries/objects, sets


# Integers(Immutable)
x = 5
y = x
x = x + 1   # creates a new object
print(x, y)  # Output: 6 5

# Strings(Immutable)
s = "hello"
print(s.upper())   # Output: HELLO (creates new string, doesn't change original)
print(s)           # Output: hello

#Tuples(Immutable)
t = (1, 2, 3)
# t[0] = 5   # Error: Tuples cannot be modified

# Lists(Mutable)
numbers = [1, 2, 3]
numbers.append(4)   # modifies the same list
print(numbers)      # Output: [1, 2, 3, 4]

# Dictionary(Mutable)
person = {"name": "Asad", "age": 21}
person["age"] = 22   # modifying value
print(person)        # Output: {'name': 'Asad', 'age': 22}

#Sets(Mutable)
fruits = {"apple", "banana"}
fruits.add("mango")    # modifies the same set
print(fruits)          # Output: {'apple', 'banana', 'mango'}


