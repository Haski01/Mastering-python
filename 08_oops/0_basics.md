## What is OOP?

- OOP (Object-Oriented Programming) is a programming paradigm that organizes code using classes and objects.
- Class → Blueprint (like a recipe).
- Object → Instance created from the class (like an actual cake made from recipe).

## OOP Pillars in Python

- `Encapsulation` → Hiding data inside objects.
- `Abstraction` → Exposing only necessary details.
- `Inheritance` → Child class inherits from parent class.
- `Polymorphism` → Same method works differently for different objects.

# [OOP Technical Terms in Python]

## Namespace

- 👉 A namespace is like a box where names (variables, functions, classes, objects) live.
  - Every variable you define in Python goes into some namespace.
  - It helps Python know which name belongs to what.

```py
x = 10  # stored in global namespace

def my_func():
    y = 5   # stored in function's local namespace
    print(y)

my_func()
print(x)
```

## Attribute Shadowing

- 👉 When an object’s own variable (attribute) hides a variable of the same name from its class.

```py
class Tea:
    name = "Default Tea"   # class attribute

chai = Tea()
print(chai.name)   # 👉 Default Tea (comes from class)

# Shadowing (creating object attribute with same name)
chai.name = "Masala Chai"
print(chai.name)   # 👉 Masala Chai (object attribute shadows class attribute)

print(Tea.name)    # 👉 Default Tea (class still has original)
```

`Note:-` Object’s chai.name shadows the class’s name.

## self Argument

- 👉 self is just a reference to the current object being created or used.
  - You don’t pass it manually — Python adds it automatically.
  - It lets methods access the object’s variables and methods.

```py
class Tea:
    def __init__(self, name):   # self refers to the object
        self.name = name

    def describe(self):
        return f"This is {self.name}"

chai = Tea("Ginger Tea")
print(chai.describe())   # 👉 "This is Ginger Tea"
```

## **init** Method (Constructor)

- 👉 **init** is a special method that runs automatically when you create an object.
  - It initializes (sets up) the object with given values.

```py
class Tea:
    def __init__(self, name, price):   # constructor
        self.name = name
        self.price = price

chai = Tea("Green Tea", 30)   # object created
print(chai.name)              # 👉 Green Tea
print(chai.price)             # 👉 30
```

- `HERE`
  - **init** runs automatically when chai is created.
  - It assigns values to the object.
